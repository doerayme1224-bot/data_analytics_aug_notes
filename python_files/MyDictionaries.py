print('Dictionaries')
print('-----------------------------------------------------')
myDict = {'key1':'value1', 'key2':'value2', 'key3':'vlue3'} # makes something called a dictionary, which is like a list that holds onto key value pairs
myDict # the name of the dictionary called 'myDict'
myDict['key1'] = 'mangos' # renames the first key's value from 'value1' into 'mangos'
myDict # shows us if we renamed it
myDict2 = {'k1': 147, 'k2': [14, 67, 8], 'k3': {'Cherry': 3}} # this shows us that dictionaries do not care about what you put into them *in this case we have an integer in 'k1' a list in 'k2' and a dictionary in 'k3' *dictionary_inception**
myDict2
myDict2.keys() # uses '.keys()' to show us each key that is within the dictionary
myDict2.values() # uses '.values()' to show us the value within each key
myDict2.items() # uses '.items()' to show us each key value pair *within () parenthesis*
if __name__ == '__main__':
    pass
