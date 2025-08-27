# Lesson 2 Module 3, Querying In SQL
#### Three Commands
1. `SELECT & FROM`
2. `ORDER BY`
3. `LIMIT & OFFSET`
#### `SELECT & FROM`
These clauses are essential for data querying through SQL. They let you specify the Data you want to collect and from where
**`SELECT`**
Keyword used to specify the column you want to display in the result of the query. Select all columns with `*` or specify which column
**`FROM`**
Keyword used to specify the table where you are getting your data from 
**EX:**
    `SELECT first_name, last_name`
    `FROM employees;`
    
**[Video on Querying](https://www.loom.com/share/cffad4c92fb746d0977be2d165ecdf80?sid=dd92a536-d425-4537-83e8-e99b492870f8)**
#### `ORDER BY`
Key word lets you sort results from a query 
- `ASC`: ascending
- `DESC`: descending
**EX:**
    `SELECT first_name, last_name, age`
   `FROM employees`
   `ORDER BY age DESC`

**[Video on ORDER BY](https://www.loom.com/share/097bbe4b2db840cb8ff67dff37ecdd6c?sid=b0571962-246c-433b-8d67-02f228d50bd1)**
#### `LIMIT & OFFSET`
Let you control the number of records returned by a query and where to start returning them from 
**`LIMIT`** 
Used to decide the max number of records returned. Used when you need to `LIMIT` the result to a mangeable size
**`OFFSET`**
Used with `LIMIT` to decide to skip a certain number of rows before returning the rows
**EX:**
    `SELECT first_name, last_name`
    `FROM employees`
    `ORDER BY hire_date`
    `LIMIT 5 OFFSET 10`

**[Video on LIMIT and OFFSET](https://www.loom.com/share/4e470bbe86db485e99a10b86e2b2df4c?sid=024da412-f940-4b33-a9e6-5f5ab251c885)**
