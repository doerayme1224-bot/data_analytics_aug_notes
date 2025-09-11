print ('lists') 
print('--------------------------------------------------------------------')
x = 'This is a string' # the variable 'x' is holding the value of a string *in apostrophes*
x
type(x) # type shows us that 'x' is a string
print('--------------------------------------------------------------------')
myList = ['Hello', 100, 23.47] # this is a list made with [] brackets, they hold onto a values *3 in this case* the string 'Hello', 100, and 23.47
print(myList) # this displays the list stored in 'myList'
anotherList = ['one', 'two', 'three'] # another example of a list
anotherList # the name/placeholder for the list
newList = myList + anotherList # this code combines the lists 'myList' and 'anotherList' into a single list called 'newList' using the operator '+'
newList # placeholder of the new list
type(newList) # shows us the value type *a list in this case*
print('--------------------------------------------------------------------')
cars = ['Mercedez', 'Volvo', 'Jaguar', 'BMW', "Audi"] # List with 5 values in a 'cars' variable
cars # placeholder of list
cars[1], cars[0], cars[3]
len(cars) # uses 'len()' *length* to show us the amount of values in the list
name = 'General Kenobi' # holds the string value 'General Kenobi' in 'name'
name # placeholder of string value
len(name) # shows us the length of the value in 'name'
print('--------------------------------------------------------------------')
cars[0] = 'Telsa' # changes the string value 'Mercedez' in the list into a string named 'Tesla' by using the index [0] and the variable of the list 'cars'
cars # shows us that we changed that value in the list
cars.append('Jeep') # uses '.append()' to add the string value 'Jeep' at the end of the cars list
cars # shows us if we changed the list
cars.pop() # uses '.pop()' to get rid of the string value 'Jeep' *got rid of jeep as we didn't specify an index/indicies*
cars.pop(2) # uses '.pop()' to gey rid of the string value 'Jaguar' *gets rid of that specific one as we specified which index to get rid of*
even = [2,4,6,8] # list of even numbers as 'even'
odd = [1,3,5,7,9] # list of odd numbers as 'odd'
numbers = odd + even # adds the 'even' and 'odd' lists using the opperator '+' and gives it the name 'numbers'
numbers
len(numbers) # uses 'len()' to show us the length of the list 'numbers'
sorted(numbers) # uses 'sorted()' to sort the numbers in a order *least to greatest*
numbers = [1, 74, 9, 316, 55, 36] # new list called numbers with newly assigned integer values
sorted(numbers) # uses 'sorted()' to sort the new 'numbers' list in an order *least to greatest*
if __name__ == '__main__':
    pass