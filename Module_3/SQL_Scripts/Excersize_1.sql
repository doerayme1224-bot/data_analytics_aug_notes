-- 1. Find how many distinct sets of tags there are in the products table.
a - what do I want
b - where do I want it from
c - How do I want it

select
	count(distinct tags)
from products;

-- 2. Find all the rows of purchases made from either Virginia (VA) or Wisconsin (WI).

select *
from purchases
where state in ('VA','WI');

-- 3. Find all the rows of the purchases made by people with the first name of "Johnathan".

select *
from purchases
where name like 'Johnathan %';

-- 4. How many purchases were made by people whose last name starts with an 'A'?

select *
from purchases
where name like '% A%';

-- 5. How many products cost between $10 and 30?

select count(price)
from products
where price >= 10 and price <= 30 ;

-- 6. What is the average price among Returned items, from the purchase_items table?


