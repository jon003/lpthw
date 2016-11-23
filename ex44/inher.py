class Parent(object):
  def implicit(self):
  	print "PARENT implicit()"

class Child(Parent):
#	pass
  def implicit(self):
  	print "Child implicit()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
