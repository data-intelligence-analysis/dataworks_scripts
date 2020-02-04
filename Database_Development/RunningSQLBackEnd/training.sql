Begin transaction;
CREATE TABLE Student (studentid Integer, studentname text, Primary Key (studentid));
CREATE TABLE Course (courseid Integer, coursename text, Primary Key (courseid));
CREATE TABLE Enrollment (studentid integer, courseid integer, Primary Key (studentid, courseid),
CONSTRAINT c1 foreign key(studentid) references Student(studentid), CONSTRAINT c2 foreign key(courseid)
references Course(courseid));
Commit;