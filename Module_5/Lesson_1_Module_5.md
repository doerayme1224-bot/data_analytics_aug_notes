# Intro to Python
#### Overview
- Value types
    ```python
    int
    float
    complex
    str
    bool
    list
    tuple
    dict
    set
    ```
- Arithmetic Operations
    ```python
    + addition
    - subtraction
    * multiplication
    / division
    // floor division
    % modulus
    ** exponentiation
    ```
#### History
Made by Van Rossum, started working on python in 1989 during a christams holiday, He wanted to create a language that was easy to understand
- named after a monty python production show (not the snake)
**his goals for python**
- easy
- open source
- understandable as english
- suitable for everday task/shorter development times
#### Intro to datatypes
![Image on datatypes](https://codingtemple.notion.site/image/https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A1400%2F1*QfI8H_8HplGa1v9IrrWjBA.png?table=block&id=4ea28230-97ce-44e3-a4bf-6eac2a0055da&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=2000&userId=&cache=v2)
1. Numeric Types
    - `int`(integer) whole numbers (no decimals)
    - `float` (float) real numbers including decimals
    - `complex` (complex number) Real numbers + imaginary numbers
2. Text Type
    - `str` Text or characters ''(single quotes) "" (double quotes)
3. Boolean
    - `True`
    - `False`
4. Collection Type
    - `list` Changeable sequence of values [enclosed in square beackets] 
    - `tuple` Unchangeable sequence (enclosed in parenthesis)
    - `set` sequence with unique elements {enclosed in curly braces} no repeating values, specify when you use them `set{1,2,3}`
    - `dict` (Dictionary) Mutable collection of key value pairs {also enclosed in curly braces} Keys have to be unique
#### `type()`
Checks which data type of a variable or value
**syntax:**

    ```python
    print(type(4.2)) # Outputs 'float'
    print(type(10)) # Outputs 'int'
    print(type("Hello!")) # Outputs 'string'
    ```
#### `print()`
Outputs info to the console
    - for displaying multiple results in a single cell... use print for each thing you want to output
**EX:**
```python
# Example: Checking data types of various values

# Without using print, only the last result is displayed
type(4.2)
type(10)
type("Hello!") # Outputs 'str'
```
**EX2:**
```python
# Example: Checking and displaying data types of various values

# Using print to output all results
print(type(4.2)) # Outputs 'float'
print(type(10)) # Outputs 'int'
print(type("Hello!")) # Outputs 'str'
```
#### Opperators
1. addition `+` adds numbers
2. subtraction `-` subtracts numbers
3. multiplication `*` multiplies numbers
4. division `/` divides numbers
5. floor division `//` divides number *AND* rounds down to the nearest `int`
**EX:**
```python
17 // 2  # Outputs 8
```
6. modulus `%` divides numbers *but* fetches remaondeer and not the quotient.
**EX:**
```python
18 % 10  # Outputs 8
```
7. exponentiation `**` raises number by the power of another ` 3 ** 6 ` three tot he power of six
##### Auto Type conversion
1. integer to float: arithmetic
    `3 + 2.0` results in float `5.0`
2. Division always results in float
    `4 / 2` is `2.0` not `2`
3. Floor Division
- Returns integer if both values are integers
    `5 // 2` will get `2`
- if one is a float, the result is a float (still represents floor division)
    `5.0 // 2` will get `2.0`
4. Exponents depends on the power
    `4 ** 0.5` will get `2.0`
#### Variables
1. start with letter or underscore (can't start with numbers)
2. No special characters (!, @, #, %)
3. case sensitive (`variable` and `VARIABLE` are different)
4. Avoid words that already have special meanings (`for`, `if`, `and`, etc.)
**Practices**
- Descriptive names that describe the data
- Consistant naming convention (think of `snake_case`)
**[pep 8 for good habits](https://peps.python.org/pep-0008/)**

## Do the copy lesson practice