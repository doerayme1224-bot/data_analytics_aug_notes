# Lists
#### Intro to Lists
Dynamic arrays that let us store different value types, good when we need a collection of items, defined with square barckets `[]`
![Image of a list](https://pynative.com/wp-content/uploads/2021/03/python-list.jpg)
#### Creating List
**EX:**
```python
fruits = ["apple", "banana", "cherry"] # List named fruits with string values seperatted with commas
```
**EX of Accessing List Items:**
```python
fruits = ["apple", "banana", "cherry"]
fruits[0]  # Outputs 'apple'
# this shows that we access a list Item with an index *0 outputs apple as 0 refers to the first Item in the list, which is a string "apple"*
# Other EX for indexing could be:
fruits[1]  # Outputs 'banana'
fruits[2]  # Outputs 'cherry'
# negative indexing can also be used:
fruits[-1]  # Outputs 'cherry'
```
#### Slicing Lists
Let you access specific segments of a list 
**EX of Slicing Lists:**
```python
# Creating a simple list of integers
number_list = [1, 2, 3, 4, 5]

# Creating a list of mixed data types
mixed_list = ["apple", 30, 4.5, True]

# Slicing to get the first three items

number_list[0:3] # Output will be [1, 2, 3]
# Extracts the first three elements of a list *remeber that it does not inclode the stop parameters index*, this is the same as number_list[:3] os an unspecified start defaults to 0

# Slicing every second item across the entire list

number_list[0:5:2] # Output will be [1, 3, 5]
# uses a step parameter to skip every other number with 2 *1 + 2 is 3, 3 + 2 is 5*, *Starts at 1 due to index being 0/the default*, *Includes every index except values after the 5th index*

# Slicing from the third item to the end of the list

mixed_list[2:] # Output will be [4.5, True]
# ommitts the end of an index, which means that it will due evry value after the start value 2
```
**Note on Indexing**
trying to access an index outside of the list will result in an error(Happens cause  you are trying to access elements that don't exist)
![Image of Error](https://images.surferseo.art/023956c0-38d1-41f1-9660-115d77d13162.png)
#### Modifying Lists
**EX on Adding Items:**
```python
fruits.append("orange") # uses .append() to add a string "orange" to the end of the list `fruits`

# This modifies the list in place, and therefore does not return the updated list as an output. However, the fruits list is now:

# ['apple', 'banana', 'cherry', 'orange']
```
**EX Inserting Items:**
```python
fruits.insert(1, "blueberry") # adds a value "blueberry" to the 1 index *2nd value in a list* using .insert() on the list `fruits`

# This modifies the list in place, and therefore does not return the updated list as an output. However, the fruits list is now:

# ['apple', 'blueberry', 'banana', 'cherry', 'orange']
```
**EX on Updating list value:**
```python
fruits[0] = "kiwi" # uses the fruits list and the specified index [0] to change that value from "apple" to "kiwi"

# This modifies the list in place, and therefore does not return the updated list as an output. However, the fruits list is now:

# ['kiwi', 'blueberry', 'banana', 'cherry', 'orange']
```
**EX on Removing Items:**
```python
fruits.remove("banana") # removes a value "banana" using .remove() on the list fruits 

# This modifies the list in place, and therefore does not return the updated list as an output. However, the fruits list is now:

# ['kiwi', 'blueberry', 'cherry', 'orange']
```
**Note on Lists:**
```python
fruits.remove("banana")

# The 'remove()' method deletes 'banana' from the list the first time 
# it's executed. However, running this cell again will cause an error 
# because 'banana' is no longer in the list.
```
![Picture example](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2Ffd7a57e3-2a77-42c4-9388-69b3528cbf74%2Fimage.png?table=block&id=d7435d73-76ba-4529-8b67-4176e57f61e7&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=1420&userId=&cache=v2)
**Good Practices**
- Check the current state of a list to make sure the item you want to manipulate is there
- After an action that changes the list, check the values within a list by running the list in a seperate cell to avoid errors
![resetting lists](https://cdn.disco.co/media/ezgif-4-c8d1f37d35_c25834f8-fcf9-4123-9e99-bbd1045717fc.gif) ensures that lists and other alterations are up to date
#### More list Methods
1. adding elements
- `.append()` adds specified element to the end of a list
- `.extend()` Extends list by adding all elements from an iterable
**EX:**
```python
more_colors = ['orange', 'purple']
colors.extend(more_colors)
# more_colors, with extend, now includes additional colors, Becomes: ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
```
- `.insert()` inserts element at a specified index
2. removing elements
- `.remove()` removes first occurence of an element
**EX:**
```python
colors.remove('black')
# if their is a color 'black' in the colors list, it will remove the first time that value shows up
```
- `.pop()` removes element from specified index, if none is specified, it will remove the last
**EX:**
```python
last_color = colors.pop()
# Will get rid of the value 'purple' in the colors list *removes the last value cause we didn't specify*
```
- `.clear()` Empties list of every value
**EX:**
```python
colors.clear()
# colors would now be empty
```
3. Finding elements
- `.index()` returns index of the first matched item
**EX:**
```python
colors.index('green')
# finds first position of 'green' in a list
```
- `.count()` Returns the amount of times an alement appeared in a list
**EX:**
```python
colors.count('blue')
# counts the amount of times 'blue' appears in the list
```
4. sorting and reversing
- `.sort()` Sorts list in ascending order (use `reverse=True` to sort in descending order)
- `.reverse()` Reverses elements of a list in place
**EX:**
```python
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
# Sorts numbers in ascending order [1, 1, 2, 3, 4, 5, 9]
numbers.reverse()
# reverses numbers in list [9, 5, 4, 3, 2, 1, 1]
```
5. copying
- `.copy()` creates a copy of the list
**EX:**
```python
numbers_copy = numbers.copy()
# Creates list numbers_copy from numbers *they are the same list unless altered*
```
6. Utility
- `len()` returns number of items in a list *Length*
**EX:**
```python
len(colors)  # Output: 7
```
- `sorted()` Creates new list with every item from the OG list in ascending order
**EX:**
```python
sorted_numbers = sorted(numbers)
# does not change OG list, but returns a new sorted list called `sorted_numbers`
```
- `sum()` Calculates sum of elements in a list (if values are numeric)
**EX:**
```python
total = sum(numbers)
# adds up all numbers in a list
```
- `max()`,`min()` returns the maximum or minimum value in a list
**EX:**
```python
highest = max(numbers)
lowest = min(numbers)
# finds highest and lowest value in a list called `numbers`
```
#### Utility functions with list operations
**Combining Utility Functions**
**EX:**
```python
average = sum(numbers) / len(numbers)
# calculates the average of numbers using the sum *total of each dataset* divided by the length *amount of observations*
```
**Analyzing Data**
**EX:**
```python
sorted_scores = sorted(exam_scores)
top_score = max(exam_scores)
bottom_score = min(exam_scores)
# makes a copy sorted list of exam_scores and stores it in sorted_scores, Then finds the min() and max() value within exam_scores and stores it in a variable top_score *for max()* and bottom_score *for min()* 
```
**Using `join()`**
joins all elements of a list into a string value
**EX:**
```python
# List of words
words = ["Hello", "world", "Python", "rocks"]

# Joining words with a space as separator
sentence = " ".join(words)
print(sentence)  # Output: Hello world Python rocks
```
you can specify any string as a seperator
**EX:**
```python
# Using a hyphen as the separator
hyphenated = "-".join(words)
print(hyphenated)  # Output: Hello-world-Python-rocks

# Using a newline character as the separator
asterisks = " * ".join(words)
print(asterisks) # Output: Hello * world * Python * rocks
```
#### other lists, Tips and Tricks
##### Nested Lists
Powerful feature that let you create complex data structures
**Structure:**
```python
nested_list = [1, [2, 3], [4, [5, 6]], 7]
``` 
1. understanding the structure
- `nested_list[0]`, would return `1`, the first element
- `nested_list[1]`, would return the list `[2, 3]`, the second element
- `nested_list[2]`, would return `[4, [5, 6]]`, contains an intger and a list, third element
- `nested_list[3]` returns `7`, last element
2. Accessing `6`, the innermost element
- first, access the tird element *index 2*
- Then, access the second element of the sublist `[5, 6]`
- Lastly, acceess the index of that innermost list *index 1*
**EX:**
```python
# Accessing the number 6
nested_list[2][1][1] # Output: 6
```
