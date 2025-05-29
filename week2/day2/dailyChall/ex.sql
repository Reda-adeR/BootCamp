/*
 * Query Analysis: Understanding NOT IN with NULL values
 * Tables:
 *   FirstTab: (id) values (5, 6, 7, NULL)
 *   SecondTab: (id) values (5, NULL)
 */

-- Q1: NOT IN with subquery returning only NULL
-- Important behavior: When the subquery returns NULL, NOT IN evaluates to UNKNOWN for all comparisons
-- Result: 0 (NULL comparison propagates through NOT IN)
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL);

-- Q2: NOT IN with subquery returning single non-NULL value (5)
-- Behavior: Proper comparison against a known value (5)
-- NULLs in FirstTab are ignored (standard SQL NULL handling)
-- Result: 2 (ids 6 and 7 don't match the excluded value 5)
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id = 5);

-- Q3: NOT IN with subquery returning mixed values (5, NULL)
-- Critical behavior: Presence of NULL in the subquery makes all comparisons UNKNOWN
-- This is a common SQL gotcha - NOT IN with NULLs behaves unexpectedly
-- Result: 0 (no rows satisfy the condition due to NULL contamination)
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab);

-- Q4: NOT IN with subquery explicitly excluding NULLs (returns only 5)
-- Proper approach: Filtering NULLs from the subquery makes NOT IN behave predictably
-- Result: 2 (ids 6 and 7 don't match the excluded value 5)
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NOT NULL);