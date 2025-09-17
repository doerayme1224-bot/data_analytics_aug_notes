# Logical operators
3 > 2 > 1 # what this is doing is comparing the expression (3 > 2) and then comparing that to (2 > 1)

3 > 2 < 1 # compares the expression (3 > 2) and then that to the other expression (2 < 1)

3 > 2 and 2 < 1 # shows how the previous block could be re written for the same result *it is like using an and operator on two comparison operators*

((3 > 2 and 2 < 1) or (34 < 2 or 7 > 2)) and not(90 < 3) # This code first evaluates everything in the purple parenthesis, it compares (3 > 2 and 2 < 1) *false*
# due to key word 'and' both expressions have to be true
# then you compare the expression (34 < 2 or 7 > 2) *true*
# 'or' means only one condityion has to be true
# connects the purple parenthsis statements with 'or' meaning only one of those two expressions have to be true *in this case it is true*
# uses and not with the previous statment to compare that to the expression 90 < 3 *not will mean the opposite, so this is True*
# will be true cause all the conditions are meet

len('hello') < len('hi') # compares the length of two strings using < and the numerical value made by len()

'hello' < 'hi' # shows us that we would need len() to perform this operation on strings

sum = 344 ^ 21 # converts numbers to binary then sum up bits of the number

type(sum)

print(sum)