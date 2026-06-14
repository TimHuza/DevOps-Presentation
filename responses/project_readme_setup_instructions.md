# DevOps Presentation Application Setup

This project is a professional, interactive DevOps training presentation authored by **Tim Huza**, featuring an attendee registration system with a MySQL backend.

## 🏗️ Technical Stack

- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Backend**: Node.js (Express.js)
- **Database**: MySQL 8.x
- **DB Client**: `mysql2`

## 📁 File Structure

```
devops-presentation/
├── public/
│   ├── index.html          # Main presentation (Generated Screen)
│   ├── style.css           # Custom styles
│   └── app.js              # Slide logic & form handling
├── server/
│   ├── index.js            # Express server
│   ├── routes/
│   │   └── register.js     # API endpoint
│   ├── db/
│   │   ├── connection.js   # MySQL pool
│   │   └── schema.sql      # Database DDL
│   └── middleware/
│       └── validate.js     # Validation logic
├── .env                    # DB credentials
├── package.json
└── README.md
```

## 🗄️ Database Schema

```sql
CREATE DATABASE IF NOT EXISTS devops_presentation;
USE devops_presentation;

CREATE TABLE IF NOT EXISTS attendees (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  first_name    VARCHAR(100)        NOT NULL,
  last_name     VARCHAR(100)        NOT NULL,
  email         VARCHAR(255)        NOT NULL UNIQUE,
  registered_at TIMESTAMP           DEFAULT CURRENT_TIMESTAMP
);
```

## 🚀 Setup Instructions

1. **Prerequisites**: Install [Node.js](https://nodejs.org/) (v18+) and [MySQL 8.x](https://dev.mysql.com/downloads/installer/).
2. **Database Setup**:
   ```sql
   CREATE DATABASE devops_presentation;
   CREATE USER 'devops_user'@'localhost' IDENTIFIED BY 'yourSecurePassword';
   GRANT ALL PRIVILEGES ON devops_presentation.* TO 'devops_user'@'localhost';
   FLUSH PRIVILEGES;
   ```
3. **Initialize Schema**: Run the `schema.sql` script in your MySQL client.
4. **Environment**: Create a `.env` file in the root directory:
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=devops_user
   DB_PASSWORD=yourSecurePassword
   DB_NAME=devops_presentation
   ```
5. **Install & Run**:
   ```bash
   npm install
   npm start
   ```
6. **Access**: Open `http://localhost:3000` in your browser.

## 🧭 Navigation
- **Keyboard**: Use `ArrowRight`/`ArrowDown` for next slide, `ArrowLeft`/`ArrowUp` for previous.
- **Controls**: Use the bottom navigation bar buttons or dot indicators.
- **Registration**: Click "Register as Attendee" on the title slide or navigation bar to open the sign-up form.
