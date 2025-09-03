# other types of sql joins
[[SQL]]
### Left join
it returns all rows from the left table and the matched rows from the right table (no match in the right table would make the columns for the right table return as Null values)
**EX:**
`SELECT columns`
`FROM table1`
`LEFT JOIN table2 ON table1.common_field = table2.common_field;`
columns - what you want to retrieve
table 1 & 2 - names of tables youre joining
common_field - column they share
![Picture of Left join](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2F5ce18cb4-9cc0-4450-b478-789c5e4f06a2%2FUntitled.png?table=block&id=f2946eca-38a4-412e-aa05-4ce35486adab&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=1150&userId=&cache=v2)
**EX:**
`SELECT `
`	Customers.customer_id,` 
`	Customers.first_name,`
`	Orders.amount`
`FROM Customers`
`LEFT JOIN Orders ON Customers.customer_id = Orders.customer;`
- selscts 2 fields from Customers, amd one from Orders
- retreives amount from orders table, only with customers who have matching orders
- customers without orders appear with null values in amount column
good for comprehensive reporting, when one table is more critical, but you wanna include related data from a different table
### Right join
Left join but opposite direction
**EX:**
`SELECT columns`
`FROM table1`
`RIGHT JOIN table2 ON table1.common_field = table2.common_field;`
![Right Join](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2Fe4467621-425d-44b3-a469-fac5cd7336c8%2FUntitled.png?table=block&id=c7bb578d-db8b-4624-b259-707133e54946&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=1420&userId=&cache=v2)
**EX right join:**
`SELECT`
`	Customers.customer_id, `
`	Customers.first_name,`
`	Orders.amount`
`FROM Customers`
`RIGHT JOIN Orders ON Customers.customer_id = Orders.customer;`
- orders without customer will appear with null values for customer_id and first_name
- you use them less than left join, but can be useful for clarity
**Left Join Equivalent:**
`SELECT `
 `   Customers.customer_id, `
  `  Customers.first_name,`
   ` Orders.amount`
`FROM Orders`
`LEFT JOIN Customers ON Orders.customer_id = Customers.customer_id;`
### Full outer join
Returns all rows from both tables
- good when you want to display all records
**EX:**
`SELECT columns`
`FROM table1`
`FULL OUTER JOIN table2 ON table1.common_field = table2.common_field;`
![Full outer join](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2F18adf0b7-a95b-40cc-b6ed-42d69f0abc69%2FUntitled.png?table=block&id=84e8bde2-d486-4cfc-938b-fd95e03c6a65&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=1420&userId=&cache=v2)
**EX:**
`SELECT `
`	Customers.customer_id,`
`	Customers.first_name,`
`	Orders.amount`
`FROM Customers`
`FULL OUTER JOIN Orders ON Customers.customer_id = Orders.customer;`
- Customers with no orders will have null values for amount
- orders that are not linked to any customers will have null for customer_id and first_name
Used for:
- data merging tasks (where you wanna combine info from both tables)
- when you wanna keep all records from both tables
**[These SQL joins](https://www.loom.com/share/28213d0da5694b079c30cc1453971fe1?sid=b92202dc-4d4a-4e01-893a-35496d3f3d2e)**
![Joins Visualizer](https://sql-joins.leopard.in.ua/)
### Multi-Table joins
Add aditional joins for multi table joins
**EX:**
`SELECT column1, column2, ...`
`FROM table1`
`JOIN table2 ON table1.common_column = table2.common_column`
`JOIN table3 ON table2.another_common_column = table3.another_common_column`
`WHERE conditions`
`ORDER BY column;`
**EX2:**
`SELECT`
`    Students.student_name,`
 `   Classes.class_name,`
  `  Teachers.teacher_name`
`FROM Students`
`JOIN Classes ON Students.class_id = Classes.class_id`
`JOIN Teachers ON Classes.teacher_id = Teachers.teacher_id;`
1. joins student table with classes table using class_id
2. joins classes table with teachers using teacher_id
3. selects student_name, class_name, and teacher_name to display list
good for..
- deeper insights 
- answering sophisticated questions

### Joining multiple fields
- done with compound keys
cobines different columns
- good for ensuring that connection between all data is meaningful
**EX:**
`SELECT`
`    P.country,`
 `   P.year,`
  `  P.population,`
   ` L.life_expectancy,`
`    I.income_per_person`
`FROM gapminder_population P`
`JOIN gapminder_life_expectancy L`
`    ON P.country = L.country AND P.year = L.year`
`JOIN gapminder_income_per_person I`
`    ON P.country = I.country AND P.year = I.year;`

1. the gapminder_population table is joined with gapminder_life_expectancy. the on ensures that records where country and year match between population and life expectancy tables
2. gapminder_population is joined with gapminder_income_per_person. on ensures records from population and income tables match country and year
good for..
- Consistency 
- accuracy 
- really good insights
### `UNION` and `UNION ALL`
**`UNION`** combines results of two or more select statements into one result set (ensures duplicates are removed). all `select` statements must have the same number of columns with similar data types to work with `union`
- use when you wanna combine tables while removing duplicates
**EX:**
`SELECT product_name FROM Products_A`
`UNION`
`SELECT product_name FROM Products_B;`
returns list of distinct product names from both tables, while removing duplicates
**VISUAL EX**
![Image of UNION](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2Fc0d73212-7767-4beb-98f6-191fa393a341%2FUntitled.png?table=block&id=ef5d8aa0-05a5-4f71-abb1-9bede4c85e75&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=1420&userId=&cache=v2)
**`UNION ALL`**
`Union` but it includes all duplicates
**EX:**
`SELECT product_name FROM Products_A`
`UNION ALL`
`SELECT product_name FROM Products_B;`
**VISUAL EX**
![Image of UNION ALL](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2F6efaa112-8ab6-400d-ac59-de597988dd95%2FUntitled.png?table=block&id=a42dd16f-2d25-4b1a-b3b0-00b4c18615cf&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=1420&userId=&cache=v2)
