class Parent(object):
''' Base parent class '''

  def override(self):
  	print "PARENT override()"

  def implicit(self):
  	print "PARENT implicit()"

  def altered(self):
  	print "PARENT altered()"

class Child(Parent):
''' Child class inheriting Parent, sometimes overriden '''

  # overrides the parent override class
  def override(self):
  	print "CHILD override()"

  # so this function does override the parent altered, 
  # but it calls super to give you the actual Parent function for altered
  def altered(self):
  	print "CHILD, BEFORE PARENT altered()"
  	super(Child, self).altered()
  	print "CHILD, AFTER PRENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

