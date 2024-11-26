DROP DATABASE IF EXISTS SchoolDB;
CREATE DATABASE SchoolDB;
USE SchoolDB;

CREATE TABLE Classes (
    class_id VARCHAR(10) PRIMARY KEY NOT NULL,
    class_name VARCHAR(255) NOT NULL,
    department VARCHAR(255),
    credits INT
);

CREATE TABLE Students (
    student_id INT PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Student_Classes (
    student_class_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    student_id INT,
    class_id VARCHAR(10),
    can_tutor BOOLEAN,
    tutoring_availability VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

CREATE TABLE Course_Notes (
    note_id INT PRIMARY KEY,
    class_id VARCHAR(10),
    note_title VARCHAR(255),
    content TEXT,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

CREATE TABLE Notebooks (
    notebook_id INT PRIMARY KEY,
    class_id VARCHAR(10),
    title VARCHAR(255),
    file TEXT,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);
