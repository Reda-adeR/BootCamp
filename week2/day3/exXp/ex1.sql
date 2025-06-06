-- @block
-- 1. Display the complete list of available languages
SELECT * FROM language;

-- @block
-- 2. Show all films with their corresponding language names
SELECT 
  f.title, 
  f.description, 
  l.name AS language
FROM film f
JOIN language l ON f.language_id = l.language_id;

-- @block
-- 3. List every language, including those without any associated films
SELECT 
  f.title, 
  f.description, 
  l.name AS language
FROM language l
LEFT JOIN film f ON f.language_id = l.language_id;

-- @block
-- 4. Build a table for new movie entries and populate it
CREATE TABLE new_film (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES 
('The Silent Wind'), 
('Shadows of Time'), 
('Nova Strike');

-- @block
-- 5. Set up a customer reviews table tied to new_film and language tables
CREATE TABLE customer_review (
  review_id SERIAL PRIMARY KEY,
  film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
  language_id INT REFERENCES language(language_id),
  title VARCHAR(255),
  score INT CHECK (score BETWEEN 1 AND 10),
  review_text TEXT,
  last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- @block
-- Add a couple of review entries to the table
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Amazing!', 9, 'A thrilling and emotional story.'),
(2, 2, 'Not bad', 7, 'Enjoyable but a bit slow in the middle.');

-- @block
-- 7. Remove a film entry that already has reviews
DELETE FROM new_film WHERE id = 1;