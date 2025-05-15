-- SELECT * FROM customer;

SELECT concat(first_name,' ',last_name) as full_name from customer;

select distinct create_date from customer;

select * from customer order by first_name desc;

select film_id,title,description,release_year,rental_rate from film order by rental_rate;

select * from film;

select address, phone from address where district='Texas';

select * from film where film_id in (15,150);

select film_id,title,description,length, rental_rate from film where title='Room Roman';

select film_id,title,description,length, rental_rate from film where title like '%Ro';

SELECT *
FROM film
ORDER BY replacement_cost ASC
FETCH FIRST 10 ROWS ONLY;
select * from payment;

select C.first_name,C.last_name,P.amount,P.payment_date
from customer C
inner join payment P
on C.customer_id=P.customer_id
order by C.customer_id;
select * from inventory;

select * from film where film_id not in(select film_id from inventory);



select Ci.city, Co.country from city Ci inner join country Co on Ci.country_id=Co.country_id;

-- select * from customer;
-- select * from staff;