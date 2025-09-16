# Sets, Tuples, Booleans, Dictionaries
#### Sets
Basically lists that store only unique items (no more than 1 unique value), are unordered and unindexed
**EX:**
![Image of Sets](https://pynative.com/wp-content/uploads/2021/03/python-sets.jpg)
```python
# Creating a set
my_set = {1, 2, 3, "apple", "banana"}

# Adding elements
my_set.add("orange")  # Adds a single element
my_set.update([4, 5, "grape"])  # Adds multiple elements

# Removing elements
my_set.discard("banana")  # Removes "banana" safely
my_set.remove("apple")  # Raises an error if 'apple' is not found

# Set Operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union
print(set_a | set_b)  # Outputs union of set_a and set_b
                      # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
print(set_a & set_b)  # Outputs intersection of set_a and set_b *What they share in common*
                      # {4, 5}

# Difference
print(set_a - set_b)  # Outputs elements unique elements of set_a
											# {1, 2, 3}

# Symmetric Difference
print(set_a ^ set_b)  # Outputs elements in either set_a or set_b, but not both
											# {1, 2, 3, 6, 7, 8}
```
**EX Customer Growth with Sets:**
```python
# Customers from the previous year
previous_customers = {'101', '102', '103', '104', '105'}

# Customers from the current year
current_customers = {'103', '104', '105', '106', '107'}

# Finding new customers who started buying this year
new_customers = current_customers - previous_customers

print(new_customers)  # Output: {'106', '107'}
# the operation of subtracting current_custoiomers from previous_customers helps us identify new_customers
```
#### Tuples
Like lists, but they are immutable/unchanging, meaning their elements can't be changed, added, or removed. Good when you want a datastructure that should not be modified. they are also ordered/indexed and iterable(you can use them with a loop)
![Image of Tuples](https://pynative.com/wp-content/uploads/2021/02/python-tuple.jpg)
**EX:**
```python
# Defining a tuple for an employee's full name
full_name = ("John", "Doe")

# Extracting information from the tuple
first_name, last_name = full_name

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
# using a tuple to store he first_name and last_name ensures consistent structure for each employee name, and also means that they won't be accidently modified
```
**Use Cases**
- storing data that shouldn't change
- using as keys in dictionaries due to them being unchanging
- returning multiple values from a function
#### Booleans
Named after mathmatician George Boole, `True` or `False` 
**Using Bools:**
1. direct evaluation
```python
is_active = True
print(is_active) # Output: True
```
2. comparison operations
```python
a = 5
b = 10
result = a < b
print(result)  # Output: True
```
3. logical operators
```python
print(True and False)  # Output: False
print(True or False)  # Output: True
print(not True)  # Output: False
```
Bools are good for...
- Controlling the flow of a program 
- making decisions by using code
- managing the state of conditions
**More EX:**
1. Making decisions
```python
is_student = True
if is_student:
    print("Eligible for student discount.")
else:
    print("Not eligible for discount.")
    
# Output: Eligible for student discount.
```
2. combining conditions
```python
age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("Allowed entry")
else:
    print("Entry denied")
    
# Output: "Allowed entry"
```
```python
# Change age to 16
age = 16
has_ticket = True
if age >= 18 and has_ticket:
    print("Allowed entry")
else:
    print("Entry denied")
    
# Output: "Entry denied"
```
Bools are also good for...
- Filtering Data
- Performing Checks
- Managing Algorithim Flow
#### Dictionaries
Store data with key value pairs
![Image of Dictionaries](https://pynative.com/wp-content/uploads/2021/02/dictionaries-in-python.jpg)
**Syntax:**
```python
person = {
  "first_name": "John",
  "last_name": "Doe",
  "age": 30
}
```
###### accessing data
you can refer to their keys:
```python
person["first_name"]  # Outputs: John
```
Trying to access dict values with an index gives you an error...
```python
person[0]  # Raises KeyError
```
![Error EX](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2Fa517ea1a-35f2-4e05-a0a5-06d21faf2503%2Fimage.png?table=block&id=e2a8ec16-d1a0-47dd-a5c3-48b96dc93310&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=1250&userId=&cache=v2)
###### modifying dictionaries
- adding items:
```python
person["profession"] = "Engineer"
```
- modding items:
```python
person["age"] = 31
```
- removing items:
```python
del person["age"]
```
###### Dictionary Methods
- `.keys()`
- `.values()`
- `.items()`
```python
# Example dictionary
vehicle_info = {
    "make": "Toyota",
    "model": "Corolla",
    "year": 2021
}

# Using keys()

vehicle_info.keys() # Outputs: dict_keys(['make', 'model', 'year'])


# Using values()

vehicle_info.values()  # Outputs: dict_values(['Toyota', 'Corolla', 2021])


# Using items()

vehicle_info.items()  # Outputs: dict_items([('make', 'Toyota'), ('model', 'Corolla'), ('year', 2021)])
```
**Use EX:**
```python
# Dictionary to store product prices
product_prices = {
  "Crunchwrap": 3.49,
  "Burrito": 2.99,
  "Baja Blast": 1.99
}

# Calculate total cost of one Crunchwrap and two Burritos
total_cost = product_prices["Crunchwrap"] + product_prices["Burrito"] * 2
print(f"Total cost: ${total_cost:.2f}")
```
They can get really big, like this **EX...**
```python
authors = {
    "J.R.R. Tolkien": {
        "genre": "fantasy",
        "books": [
            "The Fellowship of the Ring",
            "The Two Towers",
            "The Return of the King"
        ],
        "active": False
    },
    "Brandon Sanderson": {
        "genre": "fantasy",
        "books": [
            "The Way of Kings",
            "Words of Radiance",
            "Oathbringer"
        ],
        "active": True,
        "phone": {
            "home": "(281) 330-8004",
            "work": "(877) CASH-NOW"
        }
    },
    "Frank Herbert": {
        "genre": "science fiction",
        "books": ["Dune"],
        "phone": None,
        "active": False
    }
}
# in order to retrieve J.R.R. Tolkien's second book, you...
authors["J.R.R. Tolkien"]["books"][1] 
# access the "J.R.R. Tolkien" sub-dictionary in the 'authors' dictionary, then the list "books" in the "J.R.R. Tolkien" sub-dict, then specify the index of the book
# Outputs: "The Two Towers"

# For finding Brandon Sanderson's phone number, you...
authors["Brandon Sanderson"]["phone"]["work"] 
# access "Brandon Sanderson" sub-dictionary in the authors dictionary, then access the "phone" subdictionary in the "Brandon Sanderson" sub-dict, then the key "work" in the "phone" sub-dict
# Outputs: "(877) CASH-NOW"
```
