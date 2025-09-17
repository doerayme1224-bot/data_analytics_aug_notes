# for loops
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in my_list: # this is a for loop, what it is doing is going through each iteration/value `i` in the list `my_list`
  print(i) # in the for loop, prints each iteration value

for i in my_list:
  print(i + 2) # uses `+` and the integer `2` to add two to each value in the list

for somethignverystupid in my_list: # shows how the iteration variable can be named anything you want
  if somethignverystupid  % 2 == 0: # takes a value `somethingverystupid` dividing it by two, and seeing if the remainder is equal to 0
    print(somethignverystupid) # will only print even numbers due to the if statement

for i in my_list:
  print(i + 3) # uses + and 3 to add to each iteration

for i in my_list:
  print(i * 17) # uses * and 17 to multiply each iteration value by 17

for i in my_list:
  # print(pow(i, 5))
  print(i**5) # uses `**` and `5` to take every iterations value and multiply it to the power of 5

pow(my_list[3], 2) # uses pow() to multiply the value in the third index `4` by the power of 2

my_list

for i in range(0, len(my_list)): # for loop with range, range has 2 criteria, starts at index 0 (1), ends at the length of the list (20)
  print('Iteration #:', i+1) # prints the string 'Iteration #:' then adds 1 to that iterator `i`
  for j in range(i+1, len(my_list)): # for loop with 2 range criteria, `i+1` as the start, and the length of the list (20)
    print('The outside loop value is: ', # prints two strings with the valu of the i loop coming first, and the value of the j loop coming next
          my_list[i], 'The inner loop value is: ', my_list[j]) # the i always prints the number of the iterator in the list that you are on (index 0 of my_list is 1, so it will always print 1)
# the j iterator will print the iterators value + 1, and will do that for every value above the iterator in the list

