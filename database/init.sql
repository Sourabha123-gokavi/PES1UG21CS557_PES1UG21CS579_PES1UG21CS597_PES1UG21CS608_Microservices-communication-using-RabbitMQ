-- Check if the database exists
SELECT IF( EXISTS (SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'mydatabase'), 'Database exists', 'Database does not exist') AS db_exist;

-- If the database does not exist, create it
CREATE DATABASE IF NOT EXISTS mydatabase;

-- Switch to the newly created database
USE mydatabase;

-- Continue with the rest of your script...


-- Switch to the newly created database
USE mydatabase;

-- Create the inventory table
CREATE TABLE inventory (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(40),
    quantity INT,
    unit_price FLOAT,
    location VARCHAR(50),
    PRIMARY KEY(product_id, location)
);

-- Insert data into the inventory table
INSERT INTO inventory (product_name, quantity, unit_price, location) VALUES
    ('Product A', 100, 10.50, 'Location A'),
    ('Product B', 50, 20.25, 'Location B');

-- Create the users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    password VARCHAR(50)
);

-- Insert data into the users table
INSERT INTO users (name, password) VALUES ('abc', '123');

-- Create the orders table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT,
    productname VARCHAR(40),
    quantity INT,
    price FLOAT,
    stats VARCHAR(50) NOT NULL,
    FOREIGN KEY(userid) REFERENCES users(id) ON DELETE CASCADE
);

-- Create the health table
CREATE TABLE health (
    containername VARCHAR(60) PRIMARY KEY,
    stat VARCHAR(20) NOT NULL
);

-- Insert data into the health table
INSERT INTO health VALUES
    ('itemcreation', 'u'),
    ('stocksmanagement', 'u'),
    ('orderprocessing', 'u');

-- Create the admins table
CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    password VARCHAR(50)
);

-- Insert data into the admins table
INSERT INTO admins (name, password) VALUES ('admin', '123');
