

# ask the user for another file name.
print "Type the filename again:"
file_again = raw_input("> ")

# open the new file in the variable/file handle 'txt_again'
txt_again = open(file_again)

# a before, use the print function to print out what is read from the 
#  file using the read method.
print txt_again.read()

