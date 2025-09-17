# functions with math

def add(x=1, y=2): # function that has 2 parameters that each have default values
  '''
  Created by: The Creator
  Input: This function takes teo number parameters.
  Output: This function returns the addition of the two given number parameters.
  '''
  return f'The addition of x and y is: {x + y}'

add(2, 5) # calls function and passes 2 values to the parameters

def subtract(a=10, b=5):
  """
  Created by: Charles
  Input: This function takes two number parameters.
  Output: This function returns the subtraction of the two given number parameters.
  """
  print(f'the subtraction of a and b is: {a - b}')

subtract(12, 9)

def mult(c=8, d=7):
  """
  Created by: Charles
  Input: This function takes two number parameters.
  Output: This function returns the multiplication of the two given number parameters.
  """
  print(f'the multiplication of c and d is: {c * d}')

mult()

def division(e=45, f=9):
  """
  Created by: Charles
  Input: This function takes two number parameters.
  Output: This function returns the division of the two given number parameters, but it won't if the value of f is 0.
  """
  if f == 0:
    print('Nuh uh')
  else:
    print(f'the division of e and f is: {e / f}')

division(30, 0)

def exponent(g=10, h=5):
  """
  Created by: Charles
  Input: This function takes two number parameters.
  Output: This function returns the value of a variable g, and multiplies it to the power of the variable h.
  """
  print(f'the value of g to the power of h is: {g ** h}')

exponent(6, 8)

type(add)

help(add)

dir(add)

var = 1

dir(var)

