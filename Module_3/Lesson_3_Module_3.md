# Filtering Data With `WHERE`
#### Clauses/keywords in this Lesson
1. `WHERE`
2. `BETWEEN`
3. `IN`
4. `LIKE`
5. `IS NULL`
#### `WHERE`
querying data based on specific criteria. returns data that only meets the criteria. you specify the criteria that has to be meet
**EX:**
`SELECT first_name, last_name, age`
`FROM employees`
`WHERE age >= 30`
- returns only employees who are greater than or equal to 30
#### Comparisson Operators 
- Greater Than `>`
filters row when value in column is `>` specified value (Number)
**EX:**
`SELECT product_name, price`
`FROM products `
`WHERE price > 100;`
Returns product when Price is `>` 100

- Less Than `<`
Filters row when value in column is `<` specified value
**EX:**
`SELECT product_name, price`
`FROM products`
`WHERE price < 50`
returns product when Price is `<` 50

- Greater than/Equal to `>=`
filters row when value is `>=` specified value
**EX:**
`SELECT product_name, price`
`FROM products`
`WHERE price >= 200`
Returns products when price is 200 or `>=`

- Less Than/Equal To `<=`
Filters row when specified column is `<=` specified value
**EX:**
`SELECT product_name, price`
`FROM products`
`WHERE price <= 30`
Returns product when price is 30 or `<=`

- Not Equal To `<>` or `!=`
`<>` Traditional SQL operator
`!=` Borrowed from other Programming languages
filters out rows that aren't equal to specified value (That column won't show)
**EX:**
`SELECT first_name, last_name, department`
`FROM employees`
`WHERE department <> 'Marketing'`
or
`SELECT first_name, last_name, department`
`FROM employees`
`WHERE department != 'Marketing'`
Returns all employees who *ARE NOT* in Marketing
**[Video On Where](https://www.loom.com/share/bd7a66412707469792f86d7f59db1ca5?sid=48a69ad8-3d7f-4c25-b032-dea39779a07b)**
#### SQL Value Types
- Integer, Whole Number
- VarChar, Variable-Length String
- Date
- Boolean, True/False
#### `BETWEEN` & `IN`
**`BETWEEN`**
Used to filter data within a range 
**EX:**
`SELECT * FROM products`
`WHERE price BETWEEN 50 AND 100`
Selects products with price between 50 and 100

**`IN`**
Specify fields you want with where
**EX:**
`SELECT * FROM employees`
`WHERE department IN ('Sales', 'HR')`
Shows employees in sales and HR
**[Video On BETWEEN & IN](https://www.loom.com/share/f715d55cbd784c3aaaf16c9bfc3573b1?sid=edc63dcf-36af-4b0f-9fb0-8fd758abc939)**
#### `LIKE`
used in `WHERE` Clause to search for a pattern in the column
**Finding Patterns at the Beginning of String**
Use `LIKE` with `%` to Filter data on a specific Prefix
**EX:**
`SELECT product_name`
`FROM products`
`WHERE product_name LIKE 'Pro%'`
Returns all Entires in `products` if the `product_name` starts with the prefix `PRO`
**Finding Patterns at the Ending of String**
The approach for prefixes can also work for suffixes
**EX:**
`SELECT email`
`FROM contacts`
`WHERE email LIKE '%@example.com'`
Returns all emails in the `contacts` table that conclude with `'%@example.com'`
**Finding Patterns In Strings with case insensitivity**
**EX:**
`SELECT customer_name`
`FROM customers`
`WHERE LOWER(customer_name) LIKE '%ann%'`
Uses `LOWER()` to make `customer_name` column lowercase 
`%` Before and after `ann` seraches for the substring anywhere in the `customer_name` table
This code retuens any customer name thaat features the substring `ann`, names like Annabelle, Joanne, or Hannah will be returned
**[Video on `LIKE`](https://www.loom.com/share/60c9376a5dba4ba689b95479bb7b729d?sid=d22dd997-6a3d-4b6d-a743-660a82648d82)**
#### `IS NULL`
tests empty values (NULL values)
**EX:**
`SELECT * FROM employees`
`WHERE address IS NULL`
Slects employees who do not have an address listed
**[Video on `IS NULL`](https://www.loom.com/share/f1dd8b1eab454dfc85dcfdd140e89d29?sid=8a3a58e4-3f37-4d43-bec8-d8123a9f2b73)**
#### `AND, OR, NOT`
#### `AND`
will return values if all statements are true
**EX:**
`SELECT first_name, last_name, age`
`FROM employees`
`WHERE age >= 30 AND department = 'Sales';`
Returns only if age of employee is greater than or equal to 30, `AND` if they belong to the sales department
#### `OR`
returns values if only one statement is true
**EX:**
`SELECT first_name, last_name, age`
`FROM employees`
`WHERE department = 'Sales' OR department = 'IT';`
returns the value of an employee if they are part of the Sales department or if they are part of the IT department
#### `NOT`
negation opperator, will do the opposite of the statement
**EX1**
`SELECT first_name, last_name, department`
`FROM employees`
`WHERE NOT department = 'Marketing';`
Returns employees first name, last name, and department unless they are part of the marketing department
**EX2**
`SELECT first_name, last_name, department`
`FROM employees`
`WHERE NOT department LIKE 'Sale%';`
Returns employee details unless there is a `Sale%;` substring in their department name (like Sales)
**EX3**
`SELECT first_name, last_name, department`
`FROM employees`
`WHERE department NOT IN ('Marketing', 'Sales');`
Returns employee details unless they are part of the marketing or sales department
**[Video on `AND, OR, NOT`](https://www.loom.com/share/229233a9bd2441898fcdab409ab55f17?sid=79fca880-e811-4549-8414-086fc72b6db5)**
#### Combining Logical Operators
Apply Multiple conditions, parenthesis are importasnt as they will decide the order in which the conditions are evaluated
**EX:**
`SELECT * FROM employees`
`WHERE (age >= 30 OR age <= 20) AND NOT department = 'HR';`
Returns employees based on two conditions
- employees should be 30 or older, OR 20 an younger 
- employees will be in any department except HR
Parenthesis will tell SQL to evaluate that condition first, without parenthesis, SQL would do the `AND` condition first then the `OR` condition, which may return false results.
Parenthesis also group several conditions as on unit, think of order of operations (PEMDAS)
**EX:**
`SELECT * FROM employees`
`WHERE (department = 'IT' OR department = 'Marketing')`
`AND age >= 25`
`AND NOT position LIKE '%Manager%';`
explanation:
- `(department = 'IT' OR department = 'Marketing')`
    this condition returns employees if their department is `IT` or `Marketing` 
- `AND age >= 25`
    This conndition returns employees if their age is greater than or equal to 25
- `AND NOT position LIKE '%Manager%';`
    This condition won't return values if they have the `%Manager%` substring as part of their position
**EX:**
`SELECT * FROM employees`
`WHERE (performance_rating < 3 OR performance_rating > 8)`
`AND department = 'Sales'`
`AND region NOT IN ('East', 'North');`
explanation:
- `(performance_rating < 3 OR performance_rating > 8)`
    This returns an employee if there performance rating is less than 3 (1 or 2) or greater than 8 (9 or 10)
- `AND department = 'Sales'`
    This condition returns an employee if theyre in the sales department 
- `AND region NOT IN ('East', 'North');`
    This condition returns a value if their not in the East or North regions
**[Video on Combining Logical Operators](https://www.loom.com/share/acedf51e72fb4dd88508eb2697b36950?sid=e350de0f-e327-4b6b-8f0e-a42412576c20)**