
# and
if True and True: print "I know how 'Logical AND' works"

# with/as
#with open('output.txt', 'w') as f:
#    f.write('Hi there!')
# with/as is called a "Context Manager" and does cleanup for you, like closing a file.

#assert
# Assert is a great inline test.
# Example: assert False, "Error!"
#   That will check for False, and if it does not find that, throws "Error!"
# broken down, would look like:
#    if __debug__:
#      if not expression: raise AssertionError
testarino = False
#testarino = True
assert testarino == False, "testarino variable should be false but is not!"

# break
while True:
  break
  print 'You will never see this ever.'
  
# class
# I have no idea. This is all OOP stuff.  Some kind of generic container.
class Dudes(object):
  data = "guy"
  
print Dudes.data

# continue
for i in (0,1,2):
  print "I get printed 3 times."
  continue
  print "But I never get printed."
  
# def I used this all over.

# del "Delete from dictionary".  What is a dictionary?  Key/value pairs
mydict = {'Jon': '1', 'Joe': '2'}
username = 'Jon'
print "%s has number %r" % (username, mydict[username])
username = 'Joe'
print "%s has number %r" % (username, mydict[username])
del mydict[username]
print mydict

# elif, used a lot
# else, used a lot

# except, which is part of the try statement.

# exec, run a string as python.
command = 'print "hello"'
exec command

# finally, even if no exceptions get hit, do this anyway.  part of try.

# for, used this a lot

# from: import a specific part of a module
from sys import argv

# if, used this a lot

# import, see from, above.

# in, check for existence of item in otheritem.

# is, like ==

# lambda "create a short anonymous function"  
#def f (x): 
#  return x**2
#print f(8)
#64
# is the same as: 
#g = lambda x: x**2
#print g(8)
#64

# not: logical Not

# or: logical or

# pass: do nothing, but succeed.
# you would use this as successful 'stub code' when writing code, so you don't 
# have to stop and flush out a section.

# print, used al over

# raise, more exception handling stuff, see try.

# try: Exception handling. 

# while: endless loops, yay!

# with, see with/as above

# yield, like 'return' but for a generator.  which is a whole nother thing.


## Data types

# True 
# False
# None (no value)
# strings = store text
# numbers = stores integers
# floats = stores decimals
# lists = stores a list of things
# dicts = stores key:value mappings


''' String Escape Sequences
\\ blackslash
\' single quote
\" double quote
\a bell
\b backspace
\f formfeed
\n newline
\r carriage return
\t tab
\v vertical tab
'''

''' String formats
%d decimals, not floating points
%i same as %d
%o octal number
%u unsigned decimal
%x hexidecimal lowercase
%X hexidecimal uppercase
%e exponential notation, lowercase
%E exponential notation, uppercase
%f floating point number
%F same as %f
%g %f or %g, whichever is shorter
%G %g, but uppercase
%c character format
%r Repr format (debugging)
%s string format
%% percent sign
'''

''' Operators
+ Addition
- subtraction
* multiplication
** power of
/ division
// floor division, PYTHON3 to mimic round-down remainderless integer division
   think of it as math, where you drop the remainder on the floor.
% string interpolate or modulus
< less than
> greater than
<= less than or equal
>= greater than or equal
== equal
!= not equal
<> not equal
( ) parenthesis
[ ] list brackets
{ } dict curly braces
@ at (decorators)  waaaay too confusing for me to understand right now.
, comma
: colon
. dot
= assign equal
; semicolon
+= add and assign
-= subtract and assign
*= multiply and assign
/= divide and assign
//= floor divide and assign
%= modulus assign
**= power assign
