# exception Hnadlking

try: # Uses try to attempt to open some files that don't exist *in this case*
  file = open('sample1.txt','r')
  file.read() # attempts to read the values in `file`
  #f.write('This is a test')

except IOError: # Uses except to
  # This will only check if the file loads or not!
  print('ERROR: Could not find file to read the data')

else:
  print('File found and data ready')
  file.close()


try: # uses try as a way to do something that might give us an error without giving us an error
  number = 1/0 # tries to divide 1 by 0 *which would normally give us an error* and stores it in `number`
  print(number) # tries to print number
except ZeroDivisionError: # runs when the try condition fails *in this case it runs*
  print("hey man you cannot do this !!!!")
