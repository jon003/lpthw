# this function prints out the given quantity of cheese and crackers, with some 
#  commentary as well.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_crackers
  print "Man, that's enough for a party!"
  print "Get a blanket.\n"
  
# call the routine, pass it the numbers directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# set some variables in advance.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# call this, but pass variables instead of values.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# call the function, with static output, but with some math.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# call the function, but twiddle the variables we defined above wiht math.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# study drills
# 1. done
# 2. done
# 3. see below

def snack_math(cheese_count, amount_of_crackers):
  print "You have to eat %f crackers for each cheese" % (amount_of_crackers / amount_of_cheese)
  
snack_math(10, 50)
snack_math(amount_of_cheese, amount_of_crackers)
snack_math(99.4, 1405.2)


