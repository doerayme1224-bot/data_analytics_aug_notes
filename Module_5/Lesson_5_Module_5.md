# Control Flow & Iteration Essentials
1. Conditionals (`if`,`elif`,`else`)
2. `for` loops and `range()`
3. `break`,`continue`,`pass`
4. `while` loops
#### Intro to Conditionals
###### `If`
evaluates if a condition is true (if it is, that code block runs)
**EX:**
```python
x = 10
if x > 5:
    print("x is greater than 5")

# Output: 
# x is greater than 5
```
###### `elif`
"else if" lets you check multiple expression for how true they are. will executr code block when one of the conditions is true
###### `else`
runs when the `if` and all `elif` statements are false
**EX:**
```python
age = 20
if age < 13:
    print("child")
elif age < 20:
    print("teenager")
else:
    print("adult")

# Output: 
# adult
```
###### Combining Conditionals
can be done with operators: `and`, `or`, `not`
**EX:**
```python
a = 15
if a > 10 and a < 20:
    print("a is between 10 and 20")
    

# Output: 
# a is between 10 and 20
```
- sometimes you can't satisfy the criteria of a conditional, which results in no output...
```python
a = 25
if a > 10 and a < 20:
    print("a is between 10 and 20")
# even though `a` is greater than 10, it isn't less than 20, so it evaluates false and nothing is outputted
```
#### `for` loops
Used to iterate over sequences(Lists, Tuples, Dictionaries, Sets), lets you execute a block of code for each item in a sequence
**EX:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:

# apple
# banana
# cherry
# `fruit` is a variable name we chose for each item in `fruits` *make sure the iterator is an intuitive name*
```
**EX on a String:**
```python
for char in "banana":
    print(char)
    

# Output:

# b
# a
# n
# a
# n
# a
# prints each character of the string "banana" on a new line
# iterator is `char` for character
```
###### Counting in `for` loops 
**EX1:**
```python
sentence = "I have always admired the scarlet macaws in the Amazon."
count = 0
for char in sentence:
    if char == 'a':
        count += 1
print(f"The letter 'a' appears {count} times.")

# Output: 
# The letter 'a' appears 8 times.
```
the `+=` operator adds a number to the variable, and assigns the result back to that variable. `count += 1` is the same as `count = count +1`
###### Case sensitivity with `for` loops
`a` and `A` are seen as different characters to python, so if you want to count allower and uppercase letters together, you need to modify the text...
```python
sentence = "I have always admired the Scarlet macaws in the Amazon."
count = 0
for char in sentence.lower():  # Convert the sentence to lowercase
    if char == 'a':
        count += 1
print(f"The letter 'a' appears {count} times.")

# Output: 
# The letter 'a' appears 9 times.
# ensures capital and lowercase letters are counted as the same character
```
###### Building Strings with `For` loops
you can use `for` loops to add to strings...
```python
# Simple string
message = "Hello"

# Empty string to accumulate modified characters
new_message = ""

# Append each character twice to the new string
for char in message:
    new_message += char * 2

# Display the modified string
print(new_message)

# Output:
# "HHeelllloo"
```
###### Building Strings with Conditional Logic
we can use conditions with for loops to further build onto strings in a lot of ways...
```python
# Define a string
sentence = "Hello world"

# Empty string to accumulate results
new_sentence = ""

# Replace vowels with underscores and keep consonants
for char in sentence:
    if char.lower() in 'aeiou':
        new_sentence += '_'
    else:
        new_sentence += char

# Display the new string
print(new_sentence)

# Output:
# "H_ll_ w_rld"
```
###### Expending lists with Loops
you can use `for` loops to build onto lists...
```python
# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Empty list to store doubled values
doubled_numbers = []

# Doubling each number and adding it to the new list
for number in numbers:
    doubled_numbers.append(number * 2)

# Displaying the new list with doubled values
print(doubled_numbers) 

# Output: 

# [2, 4, 6, 8, 10]
```
you can also do...
```python
# Sneak peek into a list comprehension
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers) 

# Output: 
# [2, 4, 6, 8, 10]
```
#### range()
often used with `for` to specify the number of iterations...
```python
for i in range(5):
    print("I love Python!")

# Output:

# I love Python!
# I love Python!
# I love Python!
# I love Python!
# I love Python!
```
###### `range()` parameters
Has three parameters
- start, where the loop begins
- stop, when the loop ends
- step: the increment between each value in a sequence
1. one argument: amount of iterations
```python
for i in range(4):  # Generates 0, 1, 2, 3
    print(i)

# Output:

# 0
# 1
# 2
# 3
```
2. two argument: Start and Stop values
```python
for i in range(3, 7):  # Generates 3, 4, 5, 6
    print(i)

# Output:

# 3
# 4
# 5
# 6
```
3. three argument: Start, Stop, then Step value
```python
for i in range(1, 10, 2):  # Generates 1, 3, 5, 7, 9
    print(i)
    
# Output:

# 1
# 3
# 5
# 7
# 9
```
**Advnced EX:**
**Nested Loops** *loop in a loop*
```python
# Printing coordinates
for x in range(3): # Generates 0, 1, 2
    for y in range(3,6): # Generates 3, 4, 5
        print(f"Coordinate: ({x}, {y})")
        
# Output:

# Coordinate: (0, 3)
# Coordinate: (0, 4)
# Coordinate: (0, 5)
# Coordinate: (1, 3)
# Coordinate: (1, 4)
# Coordinate: (1, 5)
# Coordinate: (2, 3)
# Coordinate: (2, 4)
# Coordinate: (2, 5)

# this ex prints out coordinates for each position in a 3x3 grid
```
**`range()` with Conditional Logic**
```python
# Print even numbers between 1 and 10
for i in range(1, 11):
    if i % 2 == 0: # Checks if the number is even!
        print(i)

# Output:

# 2
# 4
# 6
# 8
# 10

# this only prints a number if it is even
```
#### `break`, `continue`, and `pass`
Provide control over the behavior of a loop
###### `break`
Terminates the loop entirely and goes to the first statement after the loop, used to exit a loop based on a condition
```python
for num in range(10):
    if num == 5:
        break  # Exits the loop when num is 5
```
###### `continue`
skips the rest of the code inside the loop for the current iteration and moves to the next iteration, able to skip specific conditions
```python
for num in range(10):
    if num % 2 == 0:
        continue  # Skips the even numbers
    print(num)  # Only prints odd numbers
```
###### `pass`
does nothing, used when a statement is required but no action needs to be done
```python
for num in range(10):
    if num % 2 == 0:
        pass  # Does nothing, just acts as a placeholder
    else:
        print(num)  # Prints only odd numbers
```
#### Intro to `while` Loops
will run as long as an expression/condition is true
**EX:**
```python
# Starting count at 10
count = 10

# Loop will run as long as count is greater than 0
while count > 0:
    print(count)
    count -= 1  # Decrement count by 1 each iteration

# Prints "Blast off!" after exiting the loop
print("Blast off!")
```
###### Waiting for a value with `while`
```python
# Simulated sensor reading
sensor_value = 75

# Waiting for the sensor value to drop below 50
while sensor_value >= 50:
    print("Waiting for sensor value to drop below 50...")
    sensor_value -= 5  # Simulate sensor value change

print("Sensor value is low enough to proceed.")
```