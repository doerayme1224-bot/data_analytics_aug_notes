# project 8
### Print first and last name in reverse order with a space between them

name = ("Charles", "Dillaway")
def new_name_order(name):
  """
  Creator: Charles
  Input: A tuple of names
  Output: The names in reverse order with a space between them
  """
  print(" ".join(name[::-1]))

new_name_order(name)