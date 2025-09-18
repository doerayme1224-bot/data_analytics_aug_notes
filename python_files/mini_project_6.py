# project 6
### Print multiplication table form 1 to 10

tuple_of_num_1 = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_of_num_2 = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
def mult_table(*num):
  """
  Creator: Charles
  Input: Two tuples of numbers
  Output: A multiplication table of the two tuples
  """
  for i in tuple_of_num_1:
    for j in tuple_of_num_2:
      print(i * j, end = "\t")
    print()

mult_table()