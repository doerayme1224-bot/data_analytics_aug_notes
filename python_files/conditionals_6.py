
print('-----------------------------------------------------------')
if True: # will run if if the statement is true *in this case it will always run*
    print("This is part of the if statement")
print("The if statement has finished") # shows that you have to indent thngs in a way you want *this is outside the if statement*
    # print("Not allowed")
print('-----------------------------------------------------------')
night = True # variable 'night' with the boolean 'True'
if night: # always runs as night is True
    print("It's night. Sleeping")
else: # never runs
    print("It's day. Being active.")
print("Out of the if statement")
print('-----------------------------------------------------------')
a, b, c = 100, 50, 20 # three variables with three values
if a > b and b > c: # runs if statement as long as a is greater than b and if b is greater than c *both conditions have to be true with the word and*
    print(f"{a} greater than {c}") # formated string that has the variable values
print('-----------------------------------------------------------')
client_funds, price, client_products = 110, 50, 0 # three variables, three values
if client_funds >= price: # runs statement if the 'client_funds' variable is greater than or equal to the 'price' variable *in this case it will*
    client_products += client_funds // price # what does this do??? '' // - floor division *rounds down if there is a decimal*
    client_funds %= price # what does '%=' do??? '%=' - modular operator *prints out the remainder of an operation*
    print(f"You have {client_products} product(s)") # this prints a formatted string that shows the value of the 'client_produts' variable
    print(f"You have {client_funds}$ left") # uses formatted string to shows the value of 'client_funds' variable
    # continue purchase flow
else: # this would run when the if statement is
    print("You have insufficient funds")
    # stop purchase flow