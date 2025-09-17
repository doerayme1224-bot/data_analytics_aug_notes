# Loops with grouping values
my_list = [(1,2,3), (3,4,6), (5,6,7), (7,8,8)] # a variable, my_list, storing a list of tuples
len(my_list)

for tup in my_list: # print each tuple using a `for` loop on `my_list`, and naming the iterator `tup`
    print(tup)

for a, b, c in my_list: # uses multiple iterators `a, b, c` in a `for loop on `my_list` to print out each value in each tuple
    print(a,b,c)

for a,b,c in my_list:
    print(b) # this one prints only the second iterator, which is in the middle of the tuple

for a,b,c in my_list:
    print(c)

my_dict = {"k1":1, "k2":2, "k3":3}

for i in my_dict: # shows that when we try to print a dictionary in a for loop and we only use one iterator, it'll print out the key
    print(i)

for i in my_dict.items(): # uses `.itmes()` to show each key:value pair
    print(i)


my_dict.items()

for a,b in my_dict.items(): # uses two iterators to, a is the key, b is the value, and uses b in the print statement to only look at the value
    print(b)


for i in my_dict.values(): # I found out how to use .values() to show just the values of a dictionary
    print(i)

