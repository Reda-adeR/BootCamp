
CREATE TABLE students (
    id_student SERIAL,
    last_name  VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    birth_date DATE NOT NULL,
    PRIMARY KEY (id_student) 
);


INSERT INTO students (last_name, first_name, birth_date) VALUES
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03');


INSERT INTO students (last_name, first_name, birth_date) 
VALUES ('ana', 'houwa', '1665-03-15')
RETURNING id_student;


SELECT * FROM students;

SELECT first_name,last_name FROM students;


SELECT first_name,last_name FROM students WHERE id_student = 2;

SELECT * FROM students WHERE first_name = 'Benichou' AND last_name = 'Marc';

SELECT * FROM students WHERE first_name = 'Benichou' OR last_name = 'March';

SELECT * FROM students WHERE last_name ILIKE '%a%';

SELECT * FROM students WHERE last_name ILIKE 'a%';

SELECT * FROM students WHERE last_name ILIKE '%a';

SELECT * FROM students WHERE last_name ILIKE '__a%';

SELECT * FROM students WHERE id_student IN (1, 3);

SELECT * FROM students WHERE birth_date >= '1998-10-10';

