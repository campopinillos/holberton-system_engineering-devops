-- Script that prepares a MySQL server for the project:
CREATE DATABASE
IF NOT EXISTS tyrell_corp;
CREATE TABLE
IF NOT EXISTS tyrell_corp.nexus6
(
	id INT,
	name VARCHAR(256));
GRANT SELECT ON tyrell_corp . * TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
INSERT INTO tyrell_corp.nexus6 (id, name) VALUES (1, 'Leon');

