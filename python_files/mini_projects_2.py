print('mini project 2')
print('----------------------------------')
vowels = ("a","e","i","o","u") # tuple of vowels
message = input("Enter the message: ") # stores an input message in a variable 'message'
new_message = "" # a string value with no value
for letters in message: # runs through every character made in the input 'message'
    if letters not in vowels: # if statement runs if the letter is not in the tuple 'vowels'
        new_message = new_message + letters # adds a letter that is not in 'vowels' to the 'new_message' value *which is nothing* *changes value of new *

print("Message without vowels is : {} ".format(new_message)) # prints the message with the formating