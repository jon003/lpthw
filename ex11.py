print "How old are you?",
age = raw_input()
print "How tall are you?", 
height = raw_input()
print "How much do you weigh?", 
weight = raw_input('---> ')

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)

# study drills
# 1 read the raw_input() docs, which is pretty short.
# 2 the passed parameter for raw_input seems to allow you to set the prompt.
# 3 see below

# new form follows
print "How old are you?"
old = raw_input('-> ')
print "You are %s years old, and you're just learning python now???" % old 