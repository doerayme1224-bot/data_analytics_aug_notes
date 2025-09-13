
print('-----------------------------------------------------------')
pet_store = ['cat', 'dog', 'rabbit'] # list nameed 'pet_store'
has_cat_food = True # variable 'has_cat_food' with a boolean 'True'

if 'cat' in pet_store: # will run if 'cat' is in the list 'pet_store' 
    print("Alright! they have a cat for me")
    if has_cat_food: # will run if 'has_cat_food' meets the condition *it will cause it is true*
        print('Buying cat and cat food')
    else: # would run if 'has_cat_food' condition wasn't meet *in this case it won't run cause 'has_cat_food' is true*
        print('Buying the cat only')
        # more code inside the else block
    # more code
else: # will run this if 'cat' isn't in 'pet_store' in this case it won't run
    print('Ask pet store to get cat')
print('-----------------------------------------------------------')
has_cat = False # variable 'has_cat' with a boolean 'False'

if has_cat: # if would run if the condition in 'has_cat' is meet *it won't cause it is false*
    pass # nothing happens, but it is herre to avoid an error
else: # will run if the condition in 'has_cat' doesn't meet the if statements requirments *in this case it will cause the variable is false*
    print("You should get a cat")
print('-----------------------------------------------------------')
has_dog = True # true
# same situation as 'has_cat' but true and pass is on 'else'
if has_dog: 
    print("Awesome!")
else:
    pass