-- 1. Select the products that cost more than average.
-- 109.0256666666666667
select 
    avg(price)
from products

select
	title,
	price
from products
where price > 109.02;

-- 2. Find all the purchase_items that represent orders for the lowest-priced product.

select *
from purchase_items
order by price desc; 

select *
from purchase_items pi2
where price = 5.99;

-- 3. Find the most recent purchase made by a user with a Gmail email address.

select 
	p.created_at,
	u.email 
from purchases p 
join users u
on p.user_id = u.user_id
where email like '%gmail.com'
order by created_at desc
limit 1;

-- 4. List the titles of the products that were ever returned in quantities greater than 4.


