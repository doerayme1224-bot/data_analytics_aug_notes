
print('-----------------------------------------------------------')
a, b = 50, 20 # makes two variables, and stores two values inside *they can be written like this*

if a > b: print("a > b") # this runs if variable a is greater than variable b

print("a > b") if a > b else print("b > a") # this will print 'a > b' if a is greater than b, but it will print 'b > a' if the conditional isn't being met

max = a if a > b else  # stores an if statment in a variable, the value will be the variable a if a is greater than b, or it will be b in any other situation
print(max) # will print the variable max