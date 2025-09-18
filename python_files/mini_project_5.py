# project 5
### Check if the first and last number of a list is the same

this_list = [1, 2, 3, 4, 5]
that_list = [1, 2, 3, 4, 1]
def check_for_equality(lst) -> None:
  """
  Creator: Charles
  Input: A list of numbers
  Output: True if the first and last number of the list are the same, False if they are not the same
  """
  if lst[0] == lst[-1]:
        print("True")
  else:
        print("False")

check_for_equality(this_list)
check_for_equality(that_list)