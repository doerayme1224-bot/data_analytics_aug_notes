

passwords = ['svakjhgjhdfgbdfg', 'asdfghjk', 'password', 'rfghj', 'ertyuik'] # list stored in 'passwords' variable
for p in passwords: # this is a for loop, it will preform a certain amount of specified iterations *in this case it will run through every value in the list until there are no more values to take*
  if p == 'password': # this if prints 'Correct password' if one or more of the iterations in the list is the value 'password'
    print('Correct password')
  else: # prints 'Try again' when thee if statements conditional isn't meet
    print('Try again')