
def cycle_numbers(max,increment):
  numbers = []
  i = 0
  
  while i < max:
    print "At the top i is %d" % i
    numbers.append(i)
  
    i = i + increment
    print "Numbers now: ", numbers
    print "At the bottom i is %d" %i
    
  print "The numbers: "

  for num in numbers: 
    print num
    
  print '\n'
    
cycle_numbers(9,1)
cycle_numbers(2,1)
cycle_numbers(10,5)
  
  
# study drills
# 1. done
# 2. done
# 3. done
# 4. done
# 5. if you rewrite for for, you don't need the increment, the for loop handles that.
  
