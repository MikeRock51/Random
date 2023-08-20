DROP USER IF EXISTS 'test'@'localhost';
CREATE USER IF NOT EXISTS 'test'@'localhost' IDENTIFIED BY 'test';
DROP DATABASE IF EXISTS attachment;
CREATE DATABASE IF NOT EXISTS attachment;
GRANT ALL PRIVILEGES ON `attachment`.* TO 'test'@'localhost';
GRANT SELECT ON `perfomance_schema`.* TO 'test'@'localhost';
FLUSH PRIVILEGES;
