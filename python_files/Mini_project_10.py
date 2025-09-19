

user_input = float(input('Please input a number'))
def computation():
  """
  Creator: Charles
  Input: float value from a user
  Output: the product of that number using the formula n+nn+nnn
  """
  new_number = (user_input + (user_input ** 2 + (user_input ** 3)))
  print(new_number)
computation()