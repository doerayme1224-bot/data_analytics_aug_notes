# functions
## Defining a function.

def my_function(): # this is a function named `my_function`
  print('Hello there') # this is an instruction stored in the function

my_function() # uses the code in the instruction by calling the function

my_function # calling the function without parenthesis will display the docstring of a function *in this case there is none*

"""
this is a
multi
line
comment
"""

def my_function2(): # function with a docstring
  """
  Created by: The creator
  Input: None
  Output: It prints 'Hello'
  """
  print('Hello')

my_function2() # uses function instruction by calling the function

my_function2 # shows doc string by calling function without ()

def greetings(name): # creates a function with a parameter/argument
  print(f'Hi there {name}') # f string with place holder name

greetings('captain') # calls function and uses parameter to pass 'captain' to the f strings place holder

def greetings(name='Tim'): # function with parameter and a deafualt value *the default prints when you don't pass a value to the string*
  print(f'Hi there {name}')

greetings() # prints the default parameter

def greetings(name='Tim'):
  return f'Hi there {name}' # uses return instead of print

greetings()

greetings("Tom") # passes tom to function parameter

import this
