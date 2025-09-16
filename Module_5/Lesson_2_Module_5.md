# Strings
Strings are sequences of characters denoted with single quotes or double quotes, they are used to store/manipulate text.
    `'hi'`, `"hi"`
    Both methods are fine, double quotes would be nice if your string already has an apostrophe
with the `print()` instruction, the quotes are removed in the output
**EX:**
```python
# Without the print function:
'Hello, world!'  # Output: 'Hello, world!'


# Using the print function:
print('Hello, world!')  # Output: Hello, world!
```
#### Escape characters
Used within strings to preform a specific action (inserting characters, moving text) 
- `\n` newline: Inserts a newline into the string where text can be displayed
    **EX:**
    ```python
    print("Line one\nLine two")
    # output:   Line one
    #           Line two
    ```
- `\t` tab: adds a horizontal tab space
    **EX:**
    ```python
    print("Name:\tJohn")
    # Output: Name:   John
    ```
- `\'` Single quote: Lets a single quote be used in a string that is made with single quotes
    **EX:**
    ```python
    print('It\'s a sunny day.')
    # Output : It's a sunny day.
    # Alternative without escape character: print("It's a sunny day.")
    ```
- `\"` double quote: Lets a double quote be used in a string made with double quotes
    **EX:**
    ```python
    print("He said, \"Hello!\"")
    # output: He said, "Hello!"
    # Alternative without escape character: print('He said, "Hello!"')
    ```
#### Multi Line Strings
For text spanning multiple lines, you use triple quotes `'''` or `"""`
**EX:**
```python
multi_line_string = """This is a string that spans
multiple lines. We can easily write text over several
lines without using escape characters for new lines."""

print(multi_line_string)
```
#### String Math
Allows us to manipulate strings 
    - Modify the string
    - combine different strings together
- Concantenation: uses `+` to combine strings
    **EX:**
    ```python
    greeting = "Hello"
    name = "Alice"
    message = greeting + ", " + name + "!"
    print(message)  # Output: Hello, Alice!
    ```
- Repitition: uses `*` in the print statement to print multiples of the string, good for creating repeating sequences and patterns
    **EX:**
    ```python
    laugh = "Ha"
    print(laugh * 10)  # Output: HaHaHaHaHaHaHaHaHaHa
    ```
#### String Methods
These let you further maniopulate text, Three common ones are...
    - `.upper()` Converts all characters in a string to be uppercase 
    - `.title()` Converts the first character for each word to be uppercase
    - `.lower()` converts all characters in a string to be lowercase
    **EX:**
```python
quote = "practice makes perfect"
print(quote.upper())  # Output: PRACTICE MAKES PERFECT
print(quote.title())  # Output: Practice Makes Perfect
print(quote.lower())  # Output: practice makes perfect
```
More advanced ones would be...
    - `.replace(old, new)` Replaces all occurences of an old substring with a new substring
    - `.split(separator)` Splits string at each instance of a separator
    **EX:**
```python
# Replacing text
sentence = "The weather is nice"
print(sentence.replace("nice", "wonderful"))  # Output: The weather is wonderful

# Splitting text
words = sentence.split(" ")
print(words)  # Output: ['The', 'weather', 'is', 'nice']
```
**on google colab, you can see all string methods by typing a string variable, then a `.` then pressing the `tab` button on your keyboard
**[String Method Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)**
#### Formatted String Literals
**F-strings** Lets you embed variables, expressions, and more into a string using `{}`
    - start with `f` or `F` then quotes `''` or `""` for string, then a value or variable inside the `{}`
**EX:**
```python
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.
```
    - can also be used with expressions
**EX:**
```python
hours = 8
rate = 15.75
pay = f"Total pay: ${hours * rate}"
print(pay)  # Output: Total pay: $126.0
```
    - format specifiers let you control how values are displayed, they follow afterr a colon `:`

**EX Rounding Numbers:**
    - you can format floats to be rounded to a specified decimal point
```python
pi = 3.1415926535
formatted_pi = f"Pi rounded to two decimal places: {pi:.2f}"
print(formatted_pi)  # Output: Pi rounded to two decimal places: 3.14
```

**EX Formatting Numbers:**
    - let you Improve readability by adding commas to numbers (for thousands places)
```python
large_number = 1000000
formatted_number = f"Formatted number: {large_number:,}"
print(formatted_number)  # Output: Formatted number: 1,000,000
```

**EX Leading zeros / signs:**
    - lets you add zeros to the left of a number
```python
quantity = 5
formatted_quantity = f"Quantity: {quantity:03d}"
print(formatted_quantity)  # Output: Quantity: 005
```
**[article on formatting f-strings](https://builtin.com/data-science/python-f-string)**
#### Indexing and Slicing with Python Strings
you can use indecies to return parts of a string (by using positive or negative numbers)
- Positive indicies start at Zero 0
- Negative Indicies start at -1 negative one
![Picture of indicies](https://www.alphacodingskills.com/python/img/python-string.png)
**EX:**
```python
word = "Python"
word[0]  # Outputs 'P'
# Accesses First Character
```
```python
word = "Python"
word[-1]  # Outputs 'n'
# Accesses Last Character
```
**More Advanced String Slicing**
using `[start:stop:step]` format Lets us slice strings
    - `start` tells us where the index while begin slicing
    - `stop` tells us where we will stop slicing
    - `step` determones the amount of characters skipped
**EX Extracting Substring:**
```python
word = "Python"
word[2:5]  # Outputs 'tho'
# Starts slice at index 2 *the third letter in Python*
# then goes up to *but does not include* the 5 index (wich is why 'n' isn't included)
```
**EX Reversing String:**
```python
word[::-1]  # Outputs 'nohtyP'
# Using step with -1 makes a string go backwards
```
**EX Skipping Characters:**
```python
word[0:6:2]  # Outputs 'Pto'
# Starts at index 0, picks every second character using a step of 2 all the way to index 5
```