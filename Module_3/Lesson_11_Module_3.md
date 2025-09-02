# Subqueries
a querry inside another SQL statement 
### Types 
- Scalar suqueries: return a single value (used with `SELECT`,`WHERE` & `HAVING`)
- Row Subqueries: Return a single row with many columns (typically with `WHERE` & `FROM`)
- Column Subqueries: Return a column and can include multiple rows (mostly `SELECT`)
- Table Subqueries: Return a full table (with `FROM`)
1. with `SELECT`
**EX:**
`SELECT `
`    name,`
`    (SELECT AVG(salary) FROM employees) AS average_salary`
`FROM departments;`
adds a column to each row that displays the average salary across employees 
2. with `WHERE`
**EX:**
`SELECT `
`    name, `
`    salary`
`FROM employees`
`WHERE salary > (SELECT AVG(salary) FROM employees);`
selects employees if their salary is above the average
3. `FROM`
**EX:**
`SELECT `
`    tmp.department_id, `
`    AVG(tmp.salary) AS average_salary`
`FROM (SELECT department_id, salary FROM employees) AS tmp`
`GROUP BY tmp.department_id;`
makes temporary view of employee salaries by department and calculates the average salary for each department 
4. Correlated subqueries
Refrences columns from outer query and runs once for each row in that query
**EX:**
`SELECT `
`    e1.name, `
`    e1.salary`
`FROM employees e1`
`WHERE e1.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id);`
Finds employees who earn more than average salary by their department
#### Best Practices
- take into account performance issues and adjust if needed
- keep your subqueries readable and use comments
- test subqueries befor nestong them in the query
**[Video On Subqueries](https://www.loom.com/share/d693dfc2e38a42999a8d68c409056f03?sid=521cd69a-63dd-44da-9e87-9166480477f7)**