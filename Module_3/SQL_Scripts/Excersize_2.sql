-- 1. Find the most recent purchase made within each state.

select 
	max(created_at),
	state
from Purchases
group by state;

-- 2. Use the purchase_items table to find the total number of each product_id sold.

select 
	product_id,
	count(quantity)
from purchase_items
group by product_id
order by product_id;

-- 3. Use the purchase_items table to see the total dollar amount of items in each state: Delivered, Returned, Pending

select 
	status,
	sum(price)       -- price * quantity for total dollar amount
from purchase_items
group by status;

-- 4. In the products table, find how many products are under each set of tags.

select 
	tags,
	count(product_id)
from products
group by tags;

-- 5. Modify the previous query to find how many products over $10 are under each set of tags.

select 
	tags,
	count(product_id)
from products
where price >= 10
group by tags;

-- 6. Use the user table to find out how many purchases each user made.



-- 7. What is the first purchase that was made in each state, in each zipcode? (No, zipcodes do not repeat between states, but write your query as though they did.)







-- 1. Find the most recent purchase made within each state.
SELECT state, MAX(created_at) 
FROM purchases
GROUP BY state;
-- 2. Use the purchase_items table to find the total number of each
--    product_id sold.
SELECT product_id, COUNT(*)
FROM purchase_items
GROUP BY product_id;


-- 3. Use the purchase_items table to see the dollar amount of items
--    in each state: Delivered, Returned, Pending
SELECT state, SUM(price * quantity)
FROM purchase_items
GROUP BY state;
-- 4. In the products table, find how many products are under each
--    set of tags.
SELECT tags, COUNT(*)
FROM products
GROUP BY tags;




-- 5. Modify the previous query to find how many products over $10
--    are under each set of tags.
SELECT tags, COUNT(*)
FROM products
WHERE price > 10
GROUP BY tags;
-- 6. Use the user table to find out how many purchases each user
--    made.
SELECT user_id, COUNT(*)
FROM purchases
GROUP BY user_id;



-- 7. What is the first purchase that was made
--    in each state, in each zipcode?
--    (No, zipcodes do not repeat between states, but
--    write your query as though they did.)
SELECT state, zipcode, MIN(created_at) FROM purchases