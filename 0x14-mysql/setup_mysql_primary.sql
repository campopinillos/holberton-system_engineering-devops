-- Script that prepares a MySQL server for the project:
CREATE USER
IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
FLUSH PRIVILEGES;

CHANGE MASTER TO MASTER_HOST='104.196.15.117', MASTER_USER='replica_user', MASTER_PASSWORD='root', MASTER_LOG_FILE='mysql-bin.000006', MASTER_LOG_POS=154;