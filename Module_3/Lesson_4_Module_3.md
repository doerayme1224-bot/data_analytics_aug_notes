# Lesson 4, Aggregating Data
[[SQL]]
Things to use in this lesson 
- `COUNT`
- `MIN`
- `MAX`
- `AVG`
- `SUM`
- `GROUP BY`
- `AS`
#### SQL's Aggregating Functions
![Image of Aggregating Functions for SQL](https://codingtemple.notion.site/image/https%3A%2F%2Fprepbytes-misc-images.s3.ap-south-1.amazonaws.com%2Fassets%2F1681468068146-1-01%20(71).png?table=block&id=8b0f42d0-aab6-40a6-ae67-33d4cdbfd10b&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=2000&userId=&cache=v2)
**COUNT**
`SELECT COUNT(employee_id)`
`FROM employees;`
counts number of employees from data table
**MIN**
`SELECT MIN(salary)`
`FROM employees;`
Returns the employee with the smallest salary
**MAX**
`SELECT MAX(salary)`
`FROM employees;`
returns the employee with the largest salary
**AVG**
`SELECT AVG(salary)`
`FROM employees;`
Returns the average salary from the employees table
**SUM**
`SELECT SUM(salary)`
`FROM employees;`
Returns the total value of the salary from the employees table
**[Video on Aggregation Functions](https://www.loom.com/share/b84b75c14eb5403d9f67018cc2d669d7?sid=990e53e4-ad3d-4c3e-8618-e52673c3695e)** 
#### `GROUP BY`
groups rows that have the same value as one another.
**EX:**
`SELECT customer_id, SUM(revenue)`
`FROM sales`
`GROUP BY customer_id;`
- groups sales by customer id
- retuens the sum of revunue for each customer
could be good at pinpointing high value customers
**EX:**
`SELECT category, COUNT(order_id)`
`FROM products`
`GROUP BY category;`
- groups products by category 
- counts number of orders for each product category
good to see which products are popular
**EX:**
`SELECT product_id, store_id, AVG(price), SUM(sales_amount)`
`FROM sales`
`GROUP BY product_id, store_id;`
- groups sales data by the products id and by the store id
- calculates the average sale price and the total sales amount for each product
good to see which products are doing well in which stores
**[Video on `GROUP BY`](https://www.loom.com/share/555e1a0c11c046cbb7b5cbcb27e0a8cc?sid=761bfd3d-4c5b-4942-9a5e-1a54c02487ef)**
#### Aliases `AS`
gives a table, or column a temporary name, good to make things more readable
**EX:**
`SELECT COUNT(employee_id) AS total_employees`
`FROM employees;`
renames `COUNT(employee_id)` to `total_employees`
**[Video On Aliasing](https://www.loom.com/share/e0f96f9e02c4487ab1d8d56ac7efa884?sid=d34df1ba-6653-4b91-bca1-062a77de21c2)**