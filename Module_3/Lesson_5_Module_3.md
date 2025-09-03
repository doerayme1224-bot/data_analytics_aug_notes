# Lesson 5 using `HAVING` with aggregates 
[[SQL]]
#### to learn 
- `HAVING`
- `DISTINCT`
#### SQL execution order
This is the order in which SQL processes queries
![Image on SQL order](https://miro.medium.com/v2/resize:fit:749/1*DN0iewN5WFWgrXs5s5cLjQ.jpeg)
- Lets your queries be relatively error free
- will help you write cleaner
#### `HAVING`
used to filter results of an agrregation query based on specific conditions: where with conditionals 
**EX:**
`SELECT department, COUNT(employee_id) AS employee_count`
`FROM employees`
`GROUP BY department`
`HAVING COUNT(employee_id) > 10;`
return departments if the count of employees is greater than 10
##### difference between `WHERE` and `HAVING`
- `WHERE`: Filters rows before groupings appled
- `HAVING`: Filters groups made by `GROUP BY` based on conditionals

**aliases and `HAVING`**
you can have aliases in `SELECT`
You can't use aliases with `HAVING` cause `HAVING` is read before `SELECT`, so they aren't yet defined
**ERROR EX:**
`SELECT department, COUNT(employee_id) AS employee_count`
`FROM employees`
`GROUP BY department`
`HAVING employee_count > 10;  -- This will cause an error`
returns error
**CORRECT EX:**
`SELECT department, COUNT(employee_id) AS employee_count`
`FROM employees`
`GROUP BY department`
`HAVING COUNT(employee_id) > 10;  -- Use the actual aggregation function`
use the aggregation function `employee_id` instead of the alias in your have statement
#### Good practices
1. use actual column name in `HAVING` clause
2. reserve aliases for `SELECT` to be clean
3. take into account SQL processing order: `FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY`
#### `DISTINCT`
Returns only unique values, eliminating duplicates entries. good to see only unique records
**EX1:**
`SELECT DISTINCT department`
`FROM employees;`
Returns all unique departments from the table
**EX2:**
`SELECT DISTINCT department, job_title`
`FROM employees;`
returns unique combos of departments and job titles from the table. 
#### Avoiding Errors
**Aggregating without grouping**
using aggregate functions without using `GROUP BY` can lead to misleading results

**CORRECT EX:**
`SELECT department, SUM(salary)`
`FROM employees`
`GROUP BY department;`
this one ensures that each departments total salary is grouped properly

**misusing `HAVING`**
Using `HAVING` without `GROUP BY`/ using it without aggregation

**CORRECT EX:**
`SELECT department, COUNT(employee_id)`
`FROM employees`
`GROUP BY department`
`HAVING COUNT(employee_id) > 5;`
uses `HAVING` properly