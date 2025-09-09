-- 1. Joins can combine more than two tables. Join the users table,  
-- purchases table, and purchase items table. Remember to use aliases.

select *
from users as u 
join purchases as p
on u.user_id = p.user_id
join purchase_items as pi
on p.purchase_id = pi.purchase_id;

-- 2. The DATEPART() function extracts whichever part of the
--  timestamp you want. E.g. DATEPART(year FROM '2001-02-16 20:38:40')
--  returns 2001. Use DATEPART() to extract which calendar month
--  each user was created in.

select date_part('month',u.created_at) as month_of_creation
from users as u;

-- 3. Use DATEPART() and a group by statement to count how many
--    users were created in each calendar month.

select 
	date_part('month',u.created_at) as month_of_creation,
	count(user_id)
from users as u
group by month_of_creation
order by month_of_creation;


-- 4. Use the DATEPART() function to find the number of users
--    created during each day of the week.
--    Hint: Use DAY as the first input

select 
	date_part('DOW', u.created_at) as Day_of_creation,
	count(user_id) as Number_of_users
from users as u
group by day_of_creation 
order by day_of_creation;


-- 5. The LEN() function will return the length of character columns.
--    Use LEN() and a group by to display the air_date in order of longest average question 
-- length to shortest average question length.



-- 6. Find the most recent purchase made by each user.

select 
	distinct p.user_id,
	max(p.created_at )
from purchases as p
group by p.user_id
order by p.user_id;

-- 7. Find the oldest purchase made by a user with a yahoo email
--    address.

select 
	distinct purchases.user_id,
	min(purchases.created_at ) as earliest_date,
	u.email 
from purchases 
join users as u 
on purchases.user_id = u.user_id
where u.email like '%@verizon.com' 
group by purchases.user_id, u.email
order by earliest_date
limit 1;

-- 8. Find all the users' emails who made at least one purchase from the
--    state of NY.

select 
	p.user_id,
	p.state,
	u.email,
	pi.quantity
from users as u 
join purchases as p
on u.user_id = p.user_id
join purchase_items as pi
on p.purchase_id = pi.purchase_id
where p.state like 'NY' and pi.quantity >= 1
group by p.user_id, p.state, u.email, pi.quantity
order by p.user_id;

-- 9. Use the DATEPART() function to find the number of users created
--    during each day of the week.
--    Hint: Use DW as the first input

select 
	date_part('DOW', u.created_at) as Day_of_creation,
	count(user_id) as Number_of_users
from users as u
group by day_of_creation 
order by day_of_creation;

-- 10. How about each day of the month?

select 
	date_part('day', u.created_at) as day_of_creation,
	count(user_id) as Number_of_users
from users as u
group by day_of_creation 
order by day_of_creation;





-- 1. Find the most recent purchase made by each user.

select 
	distinct p.user_id,
	max(p.created_at )
from purchases as p
group by p.user_id
order by p.user_id;

-- 

-- 2. Find the oldest purchase made by a user with a yahoo email address

select 
	distinct purchases.user_id,
	min(purchases.created_at ) as earliest_date,
	u.email 
from purchases 
join users as u 
on purchases.user_id = u.user_id
where u.email like '%@verizon.com' 
group by purchases.user_id, u.email
order by earliest_date
limit 1;

-- 3. Find all the users' emails who made at least one purchase from the state of NY.

select 
	p.user_id,
	p.state,
	u.email,
	pi.quantity
from users as u 
join purchases as p
on u.user_id = p.user_id
join purchase_items as pi
on p.purchase_id = pi.purchase_id
where p.state like 'NY' and pi.quantity >= 1
group by p.user_id, p.state, u.email, pi.quantity
order by p.user_id;

-- 4. Use the DATEPART() function to find the number of users created
--    during each day of the week.
--    Hint: Use DW as the first input

select 
	date_part('DOW', u.created_at) as Day_of_creation,
	count(user_id) as Number_of_users
from users as u
group by day_of_creation 
order by day_of_creation;

--SELECT DATE_PART('DOW', created_at) AS day, COUNT(*) FROM users
--GROUP BY DATE_PART('DOW', created_at) ORDER BY day; -- KHAN

-- 4b. How about each day of the month?

select 
	date_part('day', u.created_at) as Day_of_creation,
	count(user_id) as Number_of_users
from users as u
group by day_of_creation 
order by day_of_creation;



-- 2. Find the oldest purchase made by a user with a yahoo email address.
--SELECT  * FROM purchases 
--WHERE user_id IN (SELECT user_id FROM users
--WHERE email LIKE '%@gmail.com')
--ORDER BY created_at; --KHAN

--select min(p.created_at) from users u
--join purchases p 
--on u.user_id = p.user_id
--where u.email like '%@gmail.com' and p.created_at is not null; -- Daniel

--select * from users;
--select * from purchases;


--select 
--    distinct purchases.user_id,
--    min(purchases.created_at ) as earliest_date,
--    u.email 
--from purchases 
--join users as u 
--on purchases.user_id = u.user_id
--where u.email like '%@verizon.com' 
--group by purchases.user_id, u.email
--order by earliest_date
--limit 1; -- Charles

--select * from purchases as p
--join on users as u 
--where u.email like "%gmail.com%"
--order by created_at dec; --

-- 3. Find all the users' emails who made at least one purchase from the state of NY.
--SELECT * FROM users WHERE user_id IN
--(SELECT user_id FROM purchases WHERE state = 'NY');
-- OR
--SELECT * FROM users WHERE EXISTS
--(SELECT 1 FROM purchases WHERE purchases.user_id = users.user_id
--AND state = 'NY'); -- KHAN

--select u.email, count(*) from users u
--join purchases p 
--on u.user_id = p.user_id
--where p.state = 'NY'
--group by u.email
--having count(*) >= 1; -- Daniel

--select 
--    p.user_id,
--    p.state,
--    u.email,
--    pi.quantity
--from users as u 
--join purchases as p
--on u.user_id = p.user_id
--join purchase_items as pi
--on p.purchase_id = pi.purchase_id
--where p.state like 'NY' and pi.quantity >= 1
--group by p.user_id, p.state, u.email, pi.quantity
--order by p.user_id; -- Charles