

SELECT * FROM students
ORDER BY last_name
LIMIT 4;

SELECT * FROM (SELECT * FROM students LIMIT 4) AS ret
ORDER BY last_name


SELECT * FROM students ORDER BY birth_date DESC LIMIT 1;

SELECT * FROM students OFFSET 2 LIMIT 3;