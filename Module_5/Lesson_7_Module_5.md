# Functions
keyword `def`, functions allow you to put multiple code blocks into reusable instructions. They are helpful for streamlining code(making it readable and less redundant)
#### Defining and calling functions
`def name_of_function(argument):`
```python
def greet(name):
    print(f"Hello, {name}!")
# Calling the function
greet("Alice")

# Output:
# Hello, Alice 
# Calling the function
greet("Bob")

# Output:
# Hello, Bob
# the function `greet` takes the argument (name) and when the function is called, it prints a f string with the name parameter
```
#### Parameters/Arguments
Parameters are placeholders within a function and they are used to define a function
```python
def calculate_area(length, width):
    area = length * width
    return area
calculate_area(10, 5) # Output: 25
calculate_area(2, 10) # Output: 10
# function `calculate_area` takes two parameters, (length, width) to calculate the area of a rectangle. you have to pass it the two arguments 

"""
Types pf args:
- Positional: values assigned based on postion of them in the cell
- Keyword: Values assigned by naming the parameter
"""

# Calling the function with Keyword arg

calculate_area(width = 10, length = 2) # Same output, but parameters are explicitly named.
```
#### `print()` vs `return`
1. `print()`: Displays the output to the console but does not send data back to the calling of the code
2. `return`: sends data back to the caller, whioch lets you store it, manipulate it, and pass it into another function
```python
def function_print():
    print("Hello from print!")
result = function_print()
# the function `function_print` outputs the text but you can't use it any further because a value of None is returned from print *no storing in a variable*
def function_return():
    return "Hello from return!"
result = function_return()
# here, the value can be stored in `result` using return

# return EX's:
# single value
def get_double(x):
    return x * 2

# multiple values
def get_stats(numbers):
    return max(numbers), min(numbers), sum(numbers) / len(numbers)

# "capturing" returned values
doubled_value = get_double(10)  # Receives 20
max_val, min_val, avg_val = get_stats([1, 2, 3, 4, 5])  # Receives (5, 1, 3.0)
```
#### More Examples
```python
# Ex 1: Initialize
# Defining
def get_initials(first, last):
    first_init = first[0].upper()
    last_init = last[0].upper()
    return f'{first_init}.{last_init}.'
# Calling
get_initials('katie', 'sylvia') # Output: K.S.
get_initials('tom', 'hanks') # Output: T.H.
# get_initials Takes twoo arguments, (first, last) it represents first and last names of a person, takes the first character of the name using an index, and then .upper() them to make them capital letters, and lastly returns them formatted as `F.L.` 

# EX 2: Mean/Average
# def
def my_mean(nums):
    total = sum(nums)
    n = len(nums)
    return total / n
# Call
my_mean([1, 3, 4, 5]) # Output: 3.25
my_mean([85, 92, 97, 100, 88]) # Output: 92.4
# the function `my_mean(nums)` calcualtes the average within a list of numbers. takes a list called (nums) as an input, then adds them with sum(nums) 'total' and divides them by len(nums) 'amount of observations' using a return 

# EX 3: 
```