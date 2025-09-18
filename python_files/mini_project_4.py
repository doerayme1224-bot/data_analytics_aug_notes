# project 4
### Display numbers divisible by 5 from a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def divisible_by_5(lst) -> None:
  """
  Creator: Charles
  Input: A list of numbers
  Output: The numbers that are divisible by 5
  """
  for num in lst:
    if num % 5 == 0:
        print(num)

divisible_by_5(my_list)