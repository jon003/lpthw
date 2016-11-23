my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "This teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# study drill 1,2
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_centimeters = height * 2.54
weight = 180 # lbs
weight_kilograms = weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "This teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "He weighs %f kilograms and is %f centimeters tall." % (weight_kilograms, height_centimeters)

# study drill 3 answer:
# https://docs.python.org/2/library/stdtypes.html#string-formatting

