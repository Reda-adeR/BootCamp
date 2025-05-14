
--  CREATE ITEMS TABLE 

create table items(
    item_id serial PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_price SMALLINT NOT NULL
);

--  CREATE CUSTOMERS TABLE

create table customers(
    cust_id serial PRIMARY KEY,
    cust_fName VARCHAR(50) NOT NULL,
    cust_lName VARCHAR(50) NOT NULL
);

--  ADDING DATA TO ITEMS TABLE

INSERT INTO items (item_name, item_price)  
VALUES ('Small Desk', 100),
       ('Large Desk', 300);

--  ADDING DATA TO CUNSTOMERS TABLE

INSERT INTO customers (cust_fName, cust_lName)
VALUES  ('Greg', 'Jones'),
        ('hamid', 'kasri'),
        ('trevor', 'green'),
        ('trevor', 'Smith');

-- UPDATE (ADD new element )
UPDATE customers 
SET cust_lName = 'Smith' WHERE cust_id = 3;


--  SQL QUERIES TO 
    -- FETCH ALL DATA OF ITEMS
SELECT * FROM items;

    -- ITEMS WITH PRICE ABOVE 80  (FILTERING)
SELECT * FROM items WHERE item_price > 80;
SELECT * FROM items WHERE item_price < 80;
SELECT * FROM customers WHERE cust_lName = 'green';
SELECT * FROM customers WHERE cust_lName = 'Jones';
SELECT * FROM customers WHERE cust_fName != 'hamid';



       