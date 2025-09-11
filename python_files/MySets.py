print('sets')
print('---------------------------------------')
mySet = set() # created a set by typing 'set()' and stores it into 'mySet' variable
type(mySet) # uses 'type()' to show the type of value that 'mySet' is *in this case a 'set'*
mySet.add('Hello') # uses '.add()' to add the string value 'Hello' into the set
mySet
mySet.add(27) # uses '.add()' again to add the integer 27 into the set named 'mySet'
mySet
mySet
mySet.add(27) # shows that we can't reoccuring values into a set unlike a list
mySet
numbers = [1, 0, 1, 4, 4, 9, 16, 25, 25, 36] # creates a list called 'numbers' with 10 values
numbers
pnum = set(numbers) # creates a variable called 'pnum' which converts the 'numbers' list into a set with 'set()'
pnum # shows that with sets you can not have more than 1 repeating value
if __name__ == '__main__':
    pass
