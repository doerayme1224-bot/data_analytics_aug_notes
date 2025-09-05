-- 1. Join the purchases and purchase_items tables, on purchases.id and purchase_items.purchase_id 

select *
from purchases
join purchase_items 
on purchases.purchase_id = purchase_items.purchase_id;

-- 2. Modify the last query, aliasing purchases as p and purchase_items as pi.

select *
from purchases as p
join purchase_items as pi
on p.purchase_id = pi.purchase_id;

-- 3. Using the same join, perform a group by to sum the total quantity of items purchased under each user_id.

select 
	p.user_id,
	sum(pi.quantity)
from purchases as p
join purchase_items as pi
on p.purchase_id = pi.purchase_id
group by p.user_id
order by user_id;

-- 4. Using the same join, find the average purchase amount from each state.

select 
	p.state,
	avg(pi.price * pi.quantity)
from purchases as p
join purchase_items as pi
on p.purchase_id = pi.purchase_id
group by state;

-- 5. Join the purchases and users tables, using an alias for each table.

select *
from purchases as p 
join users as u
on p.user_id = u.user_id;

-- 6. Using the above join, filter to just the orders with an Gmail email address OR a buyer named 'Clay'

select *
from purchases as p 
join users as u
on p.user_id = u.user_id
where email like '%gmail.com' or name like '%Clay%';
