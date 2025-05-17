#changes.sql

-- Assignment 1 example: add a new table and column
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(5)
);

-- add a new column to an existing table
ALTER TABLE student ADD COLUMN email VARCHAR(255);

