CREATE USER 'sax'@'flask';
GRANT ALL PRIVILEGES ON *.* TO 'sax'@'flask' IDENTIFIED BY 'password' WITH GRANT OPTION;

CREATE DATABASE flask;
USE flask;

CREATE TABLE persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    Name varchar(255),
    Age int,
    PRIMARY KEY (PersonID)
);

INSERT INTO persons (Name, Age) values ("Rickard", 28);