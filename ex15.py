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

# ask the user for another file name.
print "Type the filename again:"
file_again = raw_input("> ")

# open the new file in the variable/file handle 'txt_again'
txt_again = open(file_again)

# a before, use the print function to print out what is read from the 
#  file using the read method.
print txt_again.read()

# study drills
# 1 done in this file
# 2 not stuck yet.
# ok
# 4 see file 'ex15-4.py'
# 5 see file 'ex15-5.py'
#  raw input would be good if you plan to run this interactively, or inside a user
#  interfacing loop at lot.  argv is more unix-like and if you planned to call this 
#  and pass it a parameter to run.  I tend to like the latter.
# 6 tried it.  
# 7 see below.
txt.close()
txt_again.close()
