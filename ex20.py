from sys import argv

script, input_file = argv

# new function print_all will print the whole file as read.
def print_all(f):
  print f.read()
  
# rewind uses seek to send the line number back to 0, the first line in the file.
def rewind(f):
  f.seek(0)
  
# print a line does just that, from the line number and file passed to it.  
def print_a_line(line_count, f):
  print line_count, f.readline()
  
# set the filename for the remainder of the printing exercises.  
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = 1 + 1 
print_a_line(current_line, current_file)

current_line = 1 + 1
print_a_line(current_line, current_file)

# study drills
# 1. done
# 2. done
# 3. done
# 4. seek moves the file pointer around to different lines.
#      0 is the beginning, anything else is the number of lines in.
#      second optional argument whence is neat.  
#        you can use 0 for beginning (default), 1 for current location, 2 for EOF.
# 5. += is "in place" notation for adding.  These are equivalent
#    a = a + b
#    a += b


