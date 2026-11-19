CREATE DATABASE IF NOT EXISTS db_alp;
USE db_alp;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password) VALUES 
('customer1', 'pass123'),
('customer2', 'pass456');
