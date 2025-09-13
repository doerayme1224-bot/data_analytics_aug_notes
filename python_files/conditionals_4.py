
print('-----------------------------------------------------------')
data = input("Do you have the keys? (yes/no)\n") # stores an input instruction in the variable 'data' // what is the '\n' for??? \ - escape character 'n' - new line
if data.lower() == "yes": # what is data.lower() // is it like sql lower???
    print("Starting the car")
else: # runs this condition when the if statements condition isn't meet *will print in this case*
    print("Car cannot start without the keys")
print('-----------------------------------------------------------')
data = input("Please enter the current hour (0-23):\n") # stores an input() instruction in a variable
hour = int(data) # Stores an integer of the variable 'data' in the variable 'hour' // how would this store an integer of data // is it the same as the next code block
if hour < 12: # this if statement runs if the variable 'hour' integer is less than 12
    print(f"It's {hour}am")
else: # runs this else statement if the if statement is incorrect
    print(f"It's {hour-12}pm")
print('-----------------------------------------------------------')
age = int(input("Please enter your age:\n")) # stores the integer of an input in a variable called 'age'

if age < 18: # runs this statement if the input is less than 18
    print("You are a minor")
elif age < 21: # runs this statement if the input is 18 and older, but less than 21
    print("You are an adult but cannot drink alcohol")
elif age < 35: # runs this statement if the input is 21 and older but less than 35
    print("You are younger than 35")
else: # runs this statment if none of the other conditionals are meet
    print("You are an adult")

print("If statement finished")