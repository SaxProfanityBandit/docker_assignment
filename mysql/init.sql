DROP USER IF EXISTS 'sax'@'%';
CREATE USER IF NOT EXISTS sax@'%'IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO sax@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE flask;
USE flask;

CREATE TABLE persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    Name varchar(255),
    Age int,
    PRIMARY KEY (PersonID)
);

INSERT INTO persons (Name, Age) values ("Rickard", 28);