CREATE DATABASE imc_db;
USE imc_db;
CREATE TABLE bmi_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    weight FLOAT NOT NULL,
    height FLOAT NOT NULL,
    bmi FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL
);