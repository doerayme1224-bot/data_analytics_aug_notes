print('mini project 1')
print('------------------------------------------')
num = int(input("Enter number: ")) # variable 'num' stores the integer value of an input that a user has to input
print("The numer {} in Binary value is {} ".format(num, bin(num))) # prints the binary of a number *{} are a placeholder for the .format() input* *.format is a formated string* *num in .format will print the number that a user inputted* *bin(num) takes the input and formats it as a binary*
print("The numer {} in Octal value is {} ".format(num, oct(num))) # prints the octal of a number *.format() means formatted string* *num is the integer input* *oct(num) finds the octal of the 'num'*
print("The numer {} in Hexadecimal value is {} ".format(num, hex(num))) # prints the hexadecimal of a number *.format() - formatted string* *'num' the inputted value* *hex(num) finds hexidecimal of number*
print(num) # prints the value of 'num' *the inputted value*