# Cleaning and organizing data
[[SQL]]
### Calcualated Fields 
Custom fields you create during a query. not stored in database but are created aat the time of the query.
**Use Cases**
- Numerical Calculations
- Date Manipulations
- Text Operrations
- Conditional Logic
### Numeric Calc Fields
**Use Cases**
- Performing Calculations
- Data Normalization
**EX:**
`SELECT`
`    unit_price,`
`    quantity_sold,`
`    (unit_price * quantity_sold) AS total_sales`
`FROM Sales;`
Multiplies unit_price and quantity_sold for eachh row, creating a column called total_sales that shows the total amount for each sale
### DateTime Calc Fields
**Use Cases**
- Extracting specific parts of a date
- adding/subtracting time from a given date
**EX:**
`SELECT `
`    strftime('%Y', transaction_date) AS year,`
`    strftime('%m', transaction_date) AS month,`
`    SUM(amount) AS total_amount`
`FROM Transactions`
`GROUP BY `
`     year,` 
`     month`
`ORDER BY `
`     year DESC,` 
`     month DESC;`
Extracts the year and the month from trabsaction_date and groups those resultss by the year & month
**adding days EX:**
`SELECT`
`    order_date,`
`    DATE(order_date, '+5 days') AS expected_delivery_date`
`FROM Orders;`
Uses `DATE` function to add 5 days to each order_date, calculating the expected_delivery_date
### String Calc Fields
**Use Cases**
- Data Cleaning 
- Data Enrichment 
- User-Friendly Formats (formats data in more understandable way)
- Search and Analysis (easier to filter and search through)
**Common String Functions:**
1. concantenation `||` (combines mul;tiple strings into one string)
**EX:**
`SELECT `
`     first_name || ' ' || last_name AS full_name`
`FROM Contacts;`
returns first_name and last_name as full_name
2. `TRIM` (removes specified part of string)
**EX:**
`SELECT `
`     TRIM(product_code) AS clean_product_code`
`FROM Products;`
removes unwanted spaces from product code with leading/trailing spaces
3. `UPPER` & `LOWER` (converts all text to uppercase or lowercase)
**EX:**
`SELECT `
`       UPPER(email) AS email_uppercase,`
`       LOWER(email) AS email_lowercase`
`FROM Subscribers;`
converts all email addresses to both lowercase and uppercase 
4. `SUBSTR` "Substring" extrcts a substring from the full string based on position and length 
**EX:**
`SELECT `
`     SUBSTR(telephone, 1, 3) AS area_code`
`FROM PhoneNumbers;`
Returns first three characters from telephone column labels as area code
5. `INSTR` "position of substring" Find position of specified substring within a string and returns the index of its first occurance
**EX:**
`SELECT `
`     email, `
`     INSTR(email, '@') AS at_position`
`FROM Users;`
Searches position of @ from email
## combining `INSTR` & `SUBSTR`
Good for extracting portions of a string based on its position
**EX:**
`SELECT`
`    email,`
`    SUBSTR(email, INSTR(email, '@') + 1) AS domain`
`FROM Users;`
- `INSTR(email,'@')` finds the '@' in each email
- `SUBSTR(email, INSTR(email, '@')+1)` returns the domain of email after the '@'
### `CASE` statement 
Conditional statement (like `if` `elif` `else` but for sql)
**EX:**
`SELECT`
`  student_id,`
`  score,`
`  CASE`
`    WHEN score < 50 THEN 'Fail'`
`    WHEN score BETWEEN 50 AND 69 THEN 'Pass'`
`    WHEN score BETWEEN 70 AND 89 THEN 'Good'`
`    ELSE 'Excellent'`
`  END AS performance_category`
`FROM StudentGrades;`
- categorises score into four categories:
    - WHEN score < 50 THEN 'Fail'
    - WHEN score BETWEEN 50 AND 69 THEN 'Pass'
    - WHEN score BETWEEN 70 AND 89 THEN 'Good'
    - ELSE 'Excellent' (scores above 90)
**[Video On Organizing and Cleaning Data](https://www.loom.com/share/22075aac05664fab946bb11befc0915e?sid=1108d08a-48a2-4f46-af9d-9d42e951cc5d)**