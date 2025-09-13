

response = 408 # variable with the integer 408

if response % 100 == 0: # will run this statement if the remainder of 'response' diveded by 100 is equal to 0
    print("Bad request")
elif response % 100 == 1:# will run this statement if the remainder of 'response' diveded by 100 is equal to 1
    print("Unauthorised")
elif response % 100 == 2:# will run this statement if the remainder of 'response' diveded by 100 is equal to 2
    print("Payment required")
elif response % 100 == 3:# will run this statement if the remainder of 'response' diveded by 100 is equal to 3
    print("Forbidden")
elif response % 100 == 4:# will run this statement if the remainder of 'response' diveded by 100 is equal to 4
    print("Not found")
else: # will run if none of the other conditions are met
    print("Unknown")