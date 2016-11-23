# import the argument function from the sys module
from sys import argv

# use argument 0 and 1 
# argument 0 is the name of this program.
# argument 1 is the name of the file we want to open, and is the first variable the user 
#   provides on the command line.
script, filename = argv

# open the file with the file handle/variable name "txt"
txt = open(filename)

# print out some text, and the name of the file passed on the command line.
print "Here's your file %r:" % filename

# now we're printing out the file, using the 'read' method.
print txt.read()