
print('-----------------------------------------------------------')
drink = "Tea" # variable storing a string

if drink == "Coffee": # this shows you how you can use if statements on strings to get specific  *if will run if drink holds onto the value 'Coffee'*
    print("Humanity runs on Coffee")
else: # will run if the variable 'drink' doesn't hold onto the string 'Coffee' *in this case it will cause 'drink' is holding onto the value 'Tea'
    print("Where there is a Tea, There is a hope !!!")
print('-----------------------------------------------------------')
print('Options: Coke, Coffee, Tea, Water') # this prints a string
drink = input('What woudl you like to drink? ') # this is input, which creates a box where the user has to input a value in order to return a result
print('-----------------------------------------------------------')
if drink == "Coffee": # will run the print statement if the user chose coffee
    print("Humanity runs on Coffee")
elif drink == "Water": # this is elif, it is like an in between with if and else, you can have as many elif statements as you like, this will run if the user put in water in the input
    print("Water is the soul of Earth !!!")
elif drink == "Coke": # this will run if the user put in the string coke
    print("Coke is the new fuel for the Programmer!!!")
else: # this will print if none of the other conditionals are meet *it would even work if you put in a value like "pepsi" or "dr pepper"*
    print("Where there is a Tea, There is a hope !!!")
