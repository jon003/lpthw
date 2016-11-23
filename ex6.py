
# define some variables.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print out the sums of the two variables.
print x
print y

# more text printing, invoking formatted variables with %r and %s
# %r is for 'raw data', %s formats as a string, whatever is in the variable.
# %r is best for debugging.
print "I said %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e