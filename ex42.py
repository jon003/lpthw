
# Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
  def __init__(self, meat):
    self.meat = True

## Dig is-a Animal
class Dog(Animal):

  def __init__(self, name):
    ## ??
    self.name = name
    
## Cat is-a Animal
class Cat(Animal):

  def __init__(self, name):
    ## ??
    self.name = name
    
## Person has-a name, pet
class Person(object):

  def __init__(self,name):
    ## ??
    self.name = name
    
    ## person has-a pet of some kind
    self.pet = None

## Employee is-a Person, has-a name, salary
class Employee(Person):

  def __init__(self, name, salary):
    ## ?? What is this strange magic?
    super(Employee, self).__init__(name)
    ## ??
    self.salary = salary
    
## Fish is a class.
class Fish(object):
  def __init__(self):
    self.meat = True
  
## Salmon is-a Fish
class Salmon(Fish):
  pass
    
## Halibut is-a fish
class Halibut(Fish):
  pass
  
## rover is-a Dog
rover = Dog("Rover")

## satan is-a instance of Cat with name Satan
satan = Cat("Satan")

## Mary is-a instance of Person with the name Mary
mary = Person("Mary")

## Set the mary's instance of Person's pet to satan
mary.pet = satan

## Frank is-a employee, with name Frank and Salary 120000
frank = Employee("Frank", 120000)

## set frank's pet name to rover.
frank.pet = rover

## flipper is an instance of fish.
flipper = Fish()

## crouse is-a instance of Salmon, which is-a Fish
crouse = Salmon()

## harry is-a instance of halibut which is-a Fish
harry = Halibut()


print frank.pet.name
# so the copy harry inherited the attributes from Fish.  neat.
print harry.meat  
print "%s has salary %d" % (frank.name, frank.salary)

'''
read the chapter

Study drills

1. It has to do with subclassing. some kind of backward compatibility thing.
2. dont know.
3. 

'''
