# Joining data 
### Intro to `INNER JOIN`
Combines rows from two or more tables(Based on related data between the rows)
**Syntax of `INNER JOIN`:**
`SELECT column_names`
`FROM table1`
`INNER JOIN table2`
`ON table1.common_column = table2.common_column;`
##### `INNER` is optional
**EX:**
`SELECT column_names`
`FROM table1`
`JOIN table2`
`ON table1.common_column = table2.common_column;`
This returns the same as code in "syntax of `INNER JOIN`"
Considered good practice to use inner join due to readability
**EX2:**
`SELECT`
	`Customers.customer_id,`
	`Customers.first_name,`
	`Orders.amount`
`FROM Orders`
`INNER JOIN Customers ON Orders.customer_id = Customers.customer_id;`
Shows how to use `INNER JOIN` to combine data from customers and orders table.
Retrives:
 - customer id, and first name from Customers table
- amount from orders table
- `ON`: Defines join condition Links orders.customer_id with Customers.customer_id
The order of the tables doesn't affect results (still runs unless join condition is incorrect)
### Aliasing with SQL joins
**Helpful to alias with a join when...**
- Column names are duplicated across tables
- Table names are long/hard to reference
**REALLY good for joins**
**EX:**
`SELECT`
	`c.customer_id,`
	`c.first_name,`
	`o.amount`
`FROM Orders o`
`INNER JOIN Customers c ON o.customer_id = c.customer_id;`
Orders - o
Customer - c
- `AS` is optional for joins(Orders `AS` o)
**EX2:**
`SELECT`
	`c.customer_id,`
	`c.first_name,`
	`o.date AS order_date,`
	`c.date AS customer_since`
`FROM Customers c`
`INNER JOIN Orders o ON c.customer_id = o.customer_id;`
c.date - customer_since
o.date - order_date
**[Inner join practice](https://www.loom.com/share/d39e1ef462054e4188123dfbc813c716?sid=d9241cc9-9486-497a-8ebc-c47b0775b904)**
### Agregating Data with `INNER JOINS`
**Can use `INNER JOINS` with...
- `SUM`
- `COUNT`
- `AVG` 
- + more aggregating functions
**EX:**
`SELECT` 
	`c.region,`
	`COUNT(o.order_id) AS total_orders`
`FROM customers c`
`INNER JOIN orders o`
	`ON c.customer_id = o.customer_id`
`GROUP BY c.region;`
- `SELECT` retrives region from customers & count of order_id as total_orders
- `INNER JOIN` joins c table & o table on customer_id to match customer with their order    
- `GROUP BY` groups results by region 


    `LIMIT` can limit results returned

    `ROUND(avg(o.order_id)1)`
    this is the round function

**[Aggregating Data with `INNER JOINS`](https://www.loom.com/share/1179fcf9c9cf4805b6f764764b639498?sid=475f748f-87c5-49f8-9905-dd03346a6dda)**
**[Part 2](https://www.loom.com/share/0a284994ef9d4353bfdaaa11ecbaa113?sid=9518ec6b-c784-4185-ad82-d01a2167b054)**
### using `WITH` (common table expression)
define a temporary result set that can be refrenced within a `SELECT`.
- great for breaking down complex queries into simpler parts 
**EX:**
`WITH WestCustomers AS (`
  `SELECT `
	 ` customer_id,` 
	 ` name`
`  FROM customers`
  `WHERE region = 'West'`
`)`

`SELECT `
  `name`
`FROM RegionalCustomers;`
- `WITH` defines a cte called WestCustomers, it returns customer_id and name from the customers table, filters customers by region (west)
- the main query (not the cte) retrives name from WestCustomers, given the results of the cte
- used cause of readability and reusability (meaning you can refrence it several times)
**[`WITH` Practice](https://www.loom.com/share/eccda191d2544e8aaf641de1ac6bac32?sid=bdfab4bc-2cfe-4c35-8d39-d9cfd2a72cf0)**
### database schemas
schema: design of how data is organized
- Tables 
- columns
- relationships (how tables are interconnected)
**EX:**
![Simple schema](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2Ff97dd121-3475-40b9-a77a-fecb5cf9af5f%2FUntitled.png?table=block&id=064217ae-a29f-4624-b770-30e941406780&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=2000&userId=&cache=v2)

Primary Key: Unique identifier for each record in table
- customer_id
- order_id
Foreign Key: Refrences primary key from a different table (customer_id in orders table)
**Benefits of Schemas**
- Clarity
- Organization
- Simplification
- Refrence tool
**EX**
![Complex Schema](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2Ff9098fbb-d6d1-40bf-81fb-94cca6442394%2FUntitled.png?table=block&id=9c9810a6-6754-4b97-a4a7-03d16e58be9d&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=2000&userId=&cache=v2)