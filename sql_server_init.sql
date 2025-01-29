CREATE DATABASE carrefour_db;

USE carrefour_db;

CREATE TABLE transactions (
    id INT PRIMARY KEY IDENTITY(1,1),
    value DECIMAL(10, 2),
    type VARCHAR(10),
    date DATE DEFAULT GETDATE()
);

CREATE TABLE saldo (
    id INT PRIMARY KEY IDENTITY(1,1),
    value DECIMAL(10, 2),
    date DATE DEFAULT GETDATE()
);
