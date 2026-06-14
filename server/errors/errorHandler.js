const AppError = require('./AppError');

const errorHandler = (err, req, res, next) => {
  err.statusCode = err.statusCode || 500;
  err.status = err.status || 'error';

  let errorObject = { ...err };
  errorObject.message = err.message;
  errorObject.code = err.code;

  // 1. Log the full stack trace to your terminal for development
  console.error('💥 ERROR OCCURRED:', {
    message: err.message,
    code: err.code,
    sqlState: err.sqlState,
    stack: err.stack
  });

  // 2. Translate common MySQL Database errors

  if (err.code === 'ER_NO_SUCH_TABLE') {
    errorObject = new AppError('The database table does not exist. Please run the SQL queries in MySQL Workbench.', 500);
  }

  if (err.code === 'ECONNREFUSED' || err.code === 'PROTOCOL_CONNECTION_LOST') {
    errorObject = new AppError('Could not connect to the database. Make sure MySQL Server is running.', 500);
  }

  // 3. Send the response to the browser
  res.status(errorObject.statusCode).json({
    status: errorObject.status,
    message: errorObject.message,
    // Provide technical details for debugging
    debug: {
      code: err.code || 'UNKNOWN_ERROR',
      sqlMessage: err.sqlMessage || null
    }
  });
};

module.exports = errorHandler;
