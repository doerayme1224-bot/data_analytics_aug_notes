print('intro to python')

print('-----------------------------------------------------------------------------------------------------------') # when using '---' make sure to make it a string

x = 2 # i am assigning the variable 'x' the value '2'
y = 3.5 # i am assigning the variable 'y' the value 3.5
z = x + y # i am assigning the variable 'z' the values of 'x' and 'y' and adding them with '+'

print('-----------------------------------------------------------------------------------------------------------')

print(x)
# In this line I am using the 'print()' function to print the varible 'x'
print(y)
# in this line of code I am using 'print()' to display the value of 'y'
print(z)
# in this line of code I am using 'print()' to display the value of 'z'

print('-----------------------------------------------------------------------------------------------------------')

x1 = float(x) # in this Line of code I am creating a variable 'x1' and using the function 'float()' to change the value of 'x' to a float number
print(f'The original value of the variable x is {x}, then we conrted it to {x1} usgin the built-in function float')
# in this line of code I am printing a formatted string where apostrophes are the string and the curly braces '{}' hold the variables we created previously

y1 = complex(y) # in this line of code I am creating a variable 'y1' and using the function 'complex()' to convert the variable 'y' to a complex number

print(type(x)) # This line of code uses 'print()' to display what we want, in this case the function 'type()' to get the value type of 'x' 
print(type(x1)) # this code uses 'print()' to display the 'type()' of value of variable 'x1'
print(type(y)) # this line of code uses 'print()' to display the 'type()' of value of variable'y'
print(type(y1)) # this line of code uses 'print()' to display the 'type()' of value of the variable 'y1'
print(type(z)) # this line of code uses 'print()' to display the 'type()' of value of the variable 'z'

print('-----------------------------------------------------------------------------------------------------------')

d = min(34, 67, 45, 23) # uses 'min()' on a list '(34, 67, 45, 23)' to find the smallest numerical value and stores it in the variable 'd'
print(d) # displays the variable 'd' in the console using 'print()'

r = max(34, 67, 45, 23) # uses 'max()' on a list '(34, 67, 45, 23)' to find the biggest numerical value and stores it in the variable 'r'
print(r) # displays 'r' in the console using 'print()'

w = abs(-5) # uses 'abs()' to find the absolute value of the number '-5' and stores it in the variable 'w' 
print(w) # Displays 'w' in the console using 'print()'

g = pow(4, 2) # uses 'pow()' to find the the value of '4' to the power of the exponent '2' and stores it in the variable 'g'
print(g) # displays 'g' in the console using 'print()'

print('-----------------------------------------------------------------------------------------------------------')

a = 3
b = 5
# 'a' and 'b' are variables. 'a' holds the value '3', and 'b' holds the value '5'.
c = a + b
# 'c' takes the values of 'a' and 'b' and adds them together
d = a - b
# 'd' takes the values of 'a' and 'b' and subtracts 'a' from 'b' 
e = a * b
# 'e' multiplies the value of 'a' by the value of 'b' 
f = a / b
# 'f' divides the value of 'a' by the value of 'b'
t = a ** b
# 't' takes the value of 'a' and multiplies it by itself using the value of 'b' as an exponent

print(f'The number {a} added to the number {b} is equal to the the number {c}')
# displays the formatted string in the console using 'print()', also uses '{}' as place holders in the F'string' for the variables 'a','b', and 'c'
print(f'The number {a} substracted from the number {b} is equal to the the number {d}')
# displays the formated string in the console using 'print()', also uses '{}' as place holders for the variables 'a','b', and 'd'
print(f'The number {a} multiplied to the number {b} is equal to the the number {e}')
# displays the formated string in the console using 'print()', also uses '{}' as place holders for the variables 'a','b', and 'e'
print(f'The number {a} divided by the number {b} is equal to the the number {f}')
# displays the formated string in the console using 'print()', also uses '{}' as place holders for the variables 'a','b', and 'f'
print(f'The number {a} elevated to the number {b} is equal to the the number {t}')
# displays the formated string in the console using 'print()', also uses '{}' as place holders for the variables 'a','b', and 't'

if __name__ == '__main__': # not 'as' it is '=='
    pass

# == is an assignment operator