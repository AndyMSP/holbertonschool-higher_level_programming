-- Create database and user with read-only access to it

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user and grant permissions
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';