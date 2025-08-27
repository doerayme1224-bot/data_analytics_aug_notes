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
