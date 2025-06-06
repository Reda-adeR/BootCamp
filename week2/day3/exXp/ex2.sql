-- Update a few films to use a different language by setting their language_id
UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

-- Remove the customer_review table if it exists and is no longer needed
DROP TABLE customer_review;

-- Count all rentals that haven’t been returned yet
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

-- Get the top 30 most costly films that are currently out on rental
SELECT 
  f.title, 
  f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

-- Search for a film involving a sumo storyline and featuring Penelope Monroe
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope'
  AND a.last_name = 'Monroe'
  AND f.description ILIKE '%sumo%';

-- Find a film that’s a short (under 1 hour) R-rated documentary
SELECT title
FROM film
WHERE length < 60
  AND rating = 'R'
  AND description ILIKE '%documentary%';
