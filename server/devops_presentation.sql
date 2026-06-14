CREATE DATABASE devops_presentation;
USE devops_presentation;

CREATE TABLE attendees (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100)        NOT NULL,
  last_name  VARCHAR(100)        NOT NULL,
  email      VARCHAR(255) UNIQUE NOT NULL,
  registered_at DATETIME DEFAULT CURRENT_TIMESTAMP
);