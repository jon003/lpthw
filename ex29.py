people = 20
cats = 30
dogs = 15

if people < cats:
  print "Too many cats! The world is doomed!"

if people > cats:
  print "Not too many cats! The world is saved!"
  
if people < dogs:
  print "The world is drooled on!"
  
if people > dogs:
  print "The world is dry!"
  
dogs += 5

if people >= dogs:
  print "People are greater than or equal to dogs."
  
if people <= dogs:
  print "People are less than or equal to dogs."
  
if people == dogs:
  print "People are dogs."
  
# study drills
# 1. if must check truth, and then execute the net bit IF the truth check passes
# 2. the indent separates what will be conditionally executed if the truth check passes.
# 3. it will run anyway (or throw error), because it isn't attached to the evaluation.
# 4. yup!
# 5. the truth expressions evaluate differently.
