const express = require('express');
const mysql   = require('mysql2/promise');
const cors    = require('cors');
const path    = require('path');
const fs      = require('fs');
const AppError = require('./errors/AppError');
const errorHandler = require('./errors/errorHandler');
require('dotenv').config();
const { sendInvitation } = require('./emailService');

const app = express();
app.use(cors()); // Allows register.html to talk to this server
app.use(express.json()); // Allows the server to read JSON data

// Serve the presentation HTML file at the root URL (http://localhost:3001)
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../register.html'));
});

let pool;

// Automatically create database and table if they do not exist
async function initializeDatabase() {
  try {
    // 1. Connect to MySQL server first (without database)
    const connection = await mysql.createConnection({
      host:     process.env.DB_HOST,
      port:     process.env.DB_PORT,
      user:     process.env.DB_USER,
      password: process.env.DB_PASSWORD,
    });

    // 2. Create the database if it doesn't exist
    await connection.query(`CREATE DATABASE IF NOT EXISTS \`${process.env.DB_NAME}\`;`);
    await connection.end();

    // 3. Create connection pool with database selected
    pool = mysql.createPool({
      host:     process.env.DB_HOST,
      port:     process.env.DB_PORT,
      user:     process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_NAME,
    });

    // 4. Create attendees table if it doesn't exist
    const createTableSQL = `
      CREATE TABLE IF NOT EXISTS attendees (
        id            INT AUTO_INCREMENT PRIMARY KEY,
        first_name    VARCHAR(100)        NOT NULL,
        last_name     VARCHAR(100)        NOT NULL,
        email         VARCHAR(255)        NOT NULL,
        registered_at DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `;
    await pool.execute(createTableSQL);

    // 5. Drop the unique constraint on email if it still exists from before
    //    This runs silently - if the index doesn't exist it just moves on
    try {
      await pool.execute('ALTER TABLE attendees DROP INDEX email;');
      console.log('✅ Removed unique email constraint — same email can now register again.');
    } catch (e) {
      // Index doesn't exist or was already removed — that's fine, do nothing
    }

    console.log('✅ Database & attendees table verified and ready.');
  } catch (err) {
    console.error('❌ Database Initialization Failed:');
    console.error('   Message:', err.message);
    console.error('   Code:', err.code);
    console.error('\n⚠️ Please make sure MySQL Server is running and your password in .env is correct.\n');
    process.exit(1); // Exit process because DB is required
  }
}

// Function to generate and save the CSV file
async function updateCSVExport() {
  const [rows] = await pool.execute('SELECT * FROM attendees ORDER BY registered_at DESC');
  
  const exportsDir = path.join(__dirname, 'exports');
  if (!fs.existsSync(exportsDir)) {
    fs.mkdirSync(exportsDir);
  }
  
  const csvHeaders = 'ID,First Name,Last Name,Email,Registered At\n';
  const csvRows = rows.map(row => 
    `"${row.id}","${row.first_name}","${row.last_name}","${row.email}","${new Date(row.registered_at).toLocaleString()}"`
  ).join('\n');
  
  const csvContent = csvHeaders + csvRows;
  const filePath = path.join(exportsDir, 'registrations.csv');
  
  fs.writeFileSync(filePath, csvContent);
  return filePath;
}

// The endpoint that register.html calls
app.post('/api/register', async (req, res, next) => {
  const { firstName, lastName, email } = req.body;

  if (!firstName || !lastName || !email) {
    return next(new AppError('All fields (First Name, Last Name, Email) are required.', 400));
  }

  try {
    // Insert the registration into the database table
    await pool.execute(
      'INSERT INTO attendees (first_name, last_name, email) VALUES (?, ?, ?)',
      [firstName, lastName, email]
    );

    // Send the email invitation (runs asynchronously in the background)
    sendInvitation(email, firstName).then((result) => {
      if (!result.success) {
        console.log(`ℹ️ [Registration] Completed for ${email}, but invitation email was not sent: ${result.error}`);
      }
    });

    // Automatically update the CSV file whenever a new user registers!
    await updateCSVExport();

    res.json({ success: true });
  } catch (err) {
    next(err); // Pass any SQL error to our new error handler
  }
});

// GET /api/health - Test page
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok' });
});

// GET /api/view-users - View registrations in the browser
app.get('/api/view-users', async (req, res, next) => {
  try {
    const [rows] = await pool.execute('SELECT * FROM attendees ORDER BY registered_at DESC');
    res.json(rows);
  } catch (err) {
    next(err); // Pass any SQL error to our new error handler
  }
});

// GET /api/export-csv - Saves attendees to server/exports/registrations.csv and downloads it
app.get('/api/export-csv', async (req, res, next) => {
  try {
    const filePath = await updateCSVExport();
    // Send it to the browser as a download
    res.download(filePath, 'registrations.csv');
  } catch (err) {
    next(err);
  }
});

// Global error handling middleware (must be registered last!)
app.use(errorHandler);

// Start Server after initializing database
const PORT = process.env.PORT || 3001;
async function start() {
  await initializeDatabase();
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });
}

start();