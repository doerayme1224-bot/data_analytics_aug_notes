# more on functions
def even_numbers(lst) -> list: # defines function `even_numbers` and gives it a parameter `1st`
  '''
  Created by: The Creator
  Input: This functions takes a list of digits.
  Output: This function returns a list of even numbers.
  '''
  num = [] # creates an empty list called `num`

  for x in lst: # for loop with the parameter 1st

    if x % 2 == 0: # if statment runs when the remandder of an iteration is 0

      num.append(x) # adds the value to the list


  return(num) # returns the list


even_numbers(['hello'])