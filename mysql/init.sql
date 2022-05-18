CREATE USER 'docker'@'flask';
CREATE DATABASE docker;
GRANT ALL PRIVILEGES ON *.* TO 'docker'@'flask' WITH GRANT OPTION;
FLUSH PRIVILEGES;

USE docker;

CREATE TABLE persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    Name varchar(255),
    Age int,
    PRIMARY KEY (PersonID)
);

INSERT INTO persons (Name, Age) values ("Rickard", 28);