import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '-' * 10
#assert hashmap.get(cities, 'NY') == 'Flamenco Sketches'
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

# dump city hasmap for debugging.
print '-' * 10
hashmap.dump(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
  print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

''' study drills
1. meh.

2. https://docs.python.org/2/tutorial/datastructures.html
  also http://www.tutorialspoint.com/python/python_dictionary.htm
dicts have some fun functions:  
cmp(dict1, dict2) compare elements
len(dict) length of the dictionary, the total number of items
str(dict) produces a string representation of the dict
type(variable) returns the type of the passed variable, if a dict, then will return that.
dict.clear() removes all the elements of dict.
dict.copy() returns a shallow copy of dictionary dict
dict.fromkeys() creates a new dictionary with the keys from seq and values set to value.
dict.get(key, default=None)  for specified key, return the value, or None
dict.has_key(key) returns true if key exists.
dict.items() returns a list of dict's key, value tuple pairs.
dict.keys() returns list of dictionary dict's keys
dict.setdefault(key, default=None)  similar to get() but will set dict[key]=default 
  if key is not already in dict.
dict.update(dict2) add dictionary dict2 key-value pairs to dict
dict.values()  returns a list of dictionary dict's values.

3. meh
4. assert

'''
