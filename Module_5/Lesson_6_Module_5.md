# List Comprehensions
#### Intro to List comprrehension
Provides succinct way to create lists with existing lists. more concise than for loops 
![form of list comprehension](https://media.licdn.com/dms/image/D5612AQFPLAA59HCMUA/article-cover_image-shrink_720_1280/0/1695863312592?e=2147483647&v=beta&t=HCANnY17zXaIHCswkoi6UeemLywpZcDZR7E8s1ByaJ0)
**EX1:**
```python
# Using For loop
squares = []
for i in range(10):
    squares.append(i * i)
    
print(squares)

# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# an empty list is made
# a foor loop iteratets numbers from 0 to 9, squaring the results and adding them to the list with .append()
# it is then printed


# with List Comprehension
squares = [i * i for i in range(10)]

print(squares)

# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Performs the same operation in a single line
```
###### Filtering even Numbers
**EX2:**
```python
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
        
print(evens)

# Output: [0, 2, 4, 6, 8]
# empty list, evens
# for loop iterate 0 to 9, with a conditional that checks if a number is even
# it adds that number to the list if the condition is true
# the list is printed




# with list comprehension
evens = [i for i in range(10) if i % 2 == 0]

print(evens)

# Output: [0, 2, 4, 6, 8]
# includes the conditional in the comprehension
```
###### Convert Temperatures
**EX3:**
```python
celsius = [0, 10, 20, 34.5]
fahrenheit = []
for temp in celsius:
    fahrenheit.append((temp * 9/5) + 32)
    
print(fahrenheit)

# Output: [32.0, 50.0, 68.0, 94.1]
# lists temperature values in celsius list
# empty list called fahrenheit
# for loop goes through each temp in celsius, converts them to fahrenheit with the formula (temp * 9/5) + 32 then appends that value to the fahrenheit list




# with list comprehension
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print(fahrenheit)

# Output: [32.0, 50.0, 68.0, 94.1]
```
###### Concantenating strings from a List
**EX4:**
```python
words = ['Hello', 'world', 'from', 'Python']
sentence = ''
for word in words:
    sentence += word + ' '
    
print(sentence.strip())

# Output: 'Hello world from Python'

# starts with the list `words`
# empty string called `sentence`
# iterates through each word in `words` through a for loop
# uses `.strip()` to remove a space at the end of the list `sentence`




# List Comprehension
sentence = ' '.join([word for word in words])

print(sentence)

# Output: 'Hello world from Python'
# uses `.join()` to concantenate each item in a list `words` with a ' ' *space* character
```
###### Filtering and transforming data
**EX5:**
```python
original_list = [1, -2, 3, -4, 5]
positive_doubled = []
for number in original_list:
    if number > 0:
        positive_doubled.append(number * 2)
        
print(positive_doubled)

# Output: [2, 6, 10]
# empty list: `positive_doubled`
# loops through each number in `original_list`
# checksa if each number is greater than 0, if it is, it doubles that number and appends it to a `positive_doubled`




# list comprehension
positive_doubled = [number * 2 for number in original_list if number > 0]

print(positive_doubled)

# Output: [2, 6, 10] 
# combines the iteration, condition, and the action into a single line
```
###### for strings with 'a'
**EX6:**
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
  if "a" in x:
    new_list.append(x)

print(new_list)

# Output: ["apple", "banana", "mango"]
# empty list: `new_list`
# iterates through each fruit `x` in the list `fruits`
# checks if "a" is in the name for every iteration `x`
# If it has "a", then it is added to `new_list`



# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if "a" in x]

print(new_list)

# Output: ["apple", "banana", "mango"]
```
###### other resources
**[Video on List Comprehensions](https://youtu.be/d6cwWRCysdI)**
List comprehensions become more difficult and harder to read when they start to involve more complex logic, so don't always use them over for loops
![image EX](https://miro.medium.com/v2/resize:fit:1400/0*aj3eE35fViuXCPWY.png)
#### Intro to dictionary comprehensions
**EX:**
```python
names_to_ages = {'Alice': 32, 'Bob': 36, 'Charlie': 28}

# with dictionary comprehension
ages_to_names = {value: key for key, value in names_to_ages.items()}
print(ages_to_names)

# Output: {32: 'Alice', 36: 'Bob', 28: 'Charlie'}

# here we used dictionary comprehension to swap the position of the key value pairs *think like value : key* then put them in a dictionary called `ages_to_names`
```
###### Updating values with dictionary comprehension
**EX:**
```python
# Original dictionary with employee roles
employees = {'Alice': 'Engineer', 'Bob': 'Manager', 'Charlie': 'Clerk'}

# Adding a suffix to each role
updated_employees = {key: value + " Staff" for key, value in employees.items()}
print(updated_employees)

# Output: {'Alice': 'Engineer Staff', 'Bob': 'Manager Staff', 'Charlie': 'Clerk Staff'}
# adds staff to each role and puts them in a dictionary called `updated_employees`
```