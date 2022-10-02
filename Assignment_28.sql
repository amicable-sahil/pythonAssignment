-- Q1. create a student table with 3 columns 
CREATE TABLE student (std_roll int, std_name text, std_course text);


-- Q2. Insert records for 4 students
INSERT INTO student VALUES (101, 'Sahil', 'Python'), (102, 'Jashan', 'Java'), (103, 'Preet', 'React'), (104, 'Rinku', 'Django');


-- Q3. select query to fecth all the data from students
SELECT * FROM student;


-- Q4. update name of roll no 103
UPDATE student set std_name = 'Mohan' WHERE std_roll = 103;



-- Q5. delete a record from table
DELETE FROM student WHERE std_roll = 104;




-- Q6. delete a record from table
DELETE FROM student;

-- or we can use TRUNCATE command
TRUNCATE FROM student;



-- Q7. Drop a table
DROP TABLE student;



-- Q8. Create two table and use a data if first table as foreign key in second table
CREATE Table courses(c_id int, c_name text, PRIMARY KEY(c_id));
CREATE Table students(rollno int, std_name text, c_id int, PRIMARY KEY(rollno), CONSTRAINT crs_id FOREIGN KEY(c_id) REFERENCES courses(c_id));




-- Q9. insert data in both above tables

INSERT INTO courses VALUES(1, 'Python'), (2, 'Java'), (3, 'React'), (4, 'Django');


INSERT into students VALUES(101, 'Sahil', 2), (102, 'Rinku', 4), (103, 'Preet', 1);
INSERT into students VALUES(104, 'Jashan', 2), (105, 'Kittu', 4), (106, 'Harf', 1);
INSERT into students VALUES(107, 'Meet', 3), (108, 'Rahul', 4), (109, 'Seeta', 3);



-- Q9. selecting data of a perticular couse using by course_id 
SELECT * from students where c_id = 4;