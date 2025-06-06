-- Create customer and customer_profile tables with a 1:1 relationship
CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50) NOT NULL
);

CREATE TABLE customer_profile (
  id SERIAL PRIMARY KEY,
  customer_id INT NOT NULL UNIQUE,
  is_logged_in BOOLEAN DEFAULT FALSE,
  CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customer(id)
);

-- Insert sample customers
INSERT INTO customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- Create profiles using subqueries to get customer IDs
INSERT INTO customer_profile (is_logged_in, customer_id) VALUES
(TRUE, (SELECT id FROM customer WHERE first_name = 'John')),
(FALSE, (SELECT id FROM customer WHERE first_name = 'Jerome'));

-- Get names of customers who are currently logged in
SELECT c.first_name
FROM customer c
JOIN customer_profile p ON c.id = p.customer_id
WHERE p.is_logged_in = TRUE;

-- Show all customer names along with their login status (even if no profile exists)
SELECT c.first_name, p.is_logged_in
FROM customer c
LEFT JOIN customer_profile p ON c.id = p.customer_id;

-- Count how many customers are logged in
SELECT COUNT(*) AS logged_in_count
FROM customer c
JOIN customer_profile p ON c.id = p.customer_id
WHERE p.is_logged_in = TRUE;

-- ----------------------------
-- Part II – Book lending logic
-- ----------------------------

-- Create books table
CREATE TABLE book (
  book_id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(100) NOT NULL
);

-- Insert book records
INSERT INTO book (title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To Kill a Mockingbird', 'Harper Lee');

-- Define students table with age validation
CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  age INT CHECK (age <= 15)
);

-- Add some student records
INSERT INTO student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

-- Set up library table for tracking borrowed books
CREATE TABLE library (
  book_fk_id INT,
  student_fk_id INT,
  borrowed_date DATE,
  PRIMARY KEY (book_fk_id, student_fk_id),
  FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Log borrowing activity (with subqueries)
INSERT INTO library (student_fk_id, book_fk_id, borrowed_date) VALUES
((SELECT student_id FROM student WHERE name = 'John'),
 (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
 '2022-02-15'),

((SELECT student_id FROM student WHERE name = 'Bob'),
 (SELECT book_id FROM book WHERE title = 'To Kill a Mockingbird'),
 '2021-03-03'),

((SELECT student_id FROM student WHERE name = 'Lera'),
 (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
 '2021-05-23'),

((SELECT student_id FROM student WHERE name = 'Bob'),
 (SELECT book_id FROM book WHERE title = 'Harry Potter'),
 '2021-08-12');

-- View all records from the library
SELECT * FROM library;

-- Show which students borrowed which books
SELECT s.name, b.title
FROM student s
JOIN library l ON s.student_id = l.student_fk_id
JOIN book b ON b.book_id = l.book_fk_id;

-- Calculate average age of students who borrowed "Alice In Wonderland"
SELECT AVG(s.age) AS average_age
FROM student s
JOIN library l ON s.student_id = l.student_fk_id
JOIN book b ON b.book_id = l.book_fk_id
WHERE b.title = 'Alice In Wonderland';

-- Remove a student by ID
DELETE FROM student
WHERE student_id = 1;
