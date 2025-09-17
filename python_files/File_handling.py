# file handling

fl = '/content/sample1.txt' # creates a variable `fl` that holds a value type called an _io.TextIOWrapper

my_file = open(fl) # uses open on `fl` to open the value and stores it in `my_file`

my_file.read() # uses .read() to read he opened file in `my_file`

my_file.read() # shows us that it can only read it once *it has to reset*

my_file.seek(0) # shows us how to reset the file using .seek(0) to find the begenning of the text file

my_file.read() # shows us that we reset it

type(my_file) # shows the value type of what is in `my_file`

my_file.readlines()

my_file.seek(0)

my_file.readlines() # uses .readlines() to reead out every unique line within `my_file`

