

def add_int_types(a, b):
  """

  """
  if isinstance(a, int) and isinstance(b, int):
    print(a + b)
  else:
    print('You can\'t add those')
    
add_int_types(1, 2)

add_int_types('a', 'b')

add_int_types(1, 'a')
