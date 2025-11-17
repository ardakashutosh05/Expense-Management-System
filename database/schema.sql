CREATE DATABASE IF NOT EXISTS expenses_db;

USE expenses_db;

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    amount FLOAT,
    category VARCHAR(50)
);
