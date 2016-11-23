"""
My Silly Game

takes args for adventurer name.

each room is a function.
0. exploding bomb room. 'type 42' to disarm, anything else, death.
1. beartrap room. 'disarm trap' to exit, anything else, death.
2. giant rolling ball, indiana jones style, run to exit, anything else, death.
3. sphinx room.  answer a riddle, or the sphinx eats you. success, you win game.

each successful except sphinx room invokes: random room selector

"""

from random import randint
from sys import argv
script, adventurer = argv

print "Welcome, Adventurer %s!" % adventurer

def dead(why):
  print why, "Oops!"
  exit(0)
  
def bomb_room():
  print """
  You enter a room with a pedestal in the middle.  There is a bomb on the pedestal.
  You must enter a 2 digit code.  Somebody has scratched 'the universe' into the 
  granite on the side of the pedestal.  The bomb begins counting down. 
  What do you enter? """
  code = raw_input('> ')
  if code == "42":
    print "The bomb stops counting down!  The door to the next room unlocks..."
    random_room()
  else:
    dead("The bomb explodes, taking you with it.")

def bear_room():
  print """
  You enter a narrow hallway with an unavoidable beartrap in the middle.  You need 
  to get to the far side to the door.
  How do you get past? """
  past = raw_input('> ')
  if "disarm" in past:
    print "You disarm the trap and cross safely.  The door to the next room unlocks..."
    random_room()
  elif "jump" in past:
    dead("You attempt tp jump over, but slip.  The trap takes off your head.")
  else:
    dead("Your foolish idea backfires in a hilarious death.")
  
def ball_room():
  print """
  You enter a strange alley shaped hallway.  The door locks behind you with a click. 
  Above the door is a ramp with a massive round boulder, which has just been released.
  What do you do now?"""
  whatnow = raw_input('> ')
  if whatnow == "run":
    print "You run for your life, and make it through the door to the next room..."
    random_room()
  else:
    dead("Your foolish idea backfires in a hilarious death.")
  
def sphinx_room():
  print """
  You enter a large palatial room with a huge Sphinx in the middle.  It speaks!
  Answer my riddle, or I shall consume you!  "What is the creature that walks on four 
  legs in the morning, two legs at noon and three in the evening?"
  What do you do answer?"""
  whatnow = raw_input('> ')
  if whatnow == "man":
    print """
    pyHe congratulates you, offers you as much treasure as you can carry and 
    allows you to exit and go home. """
    exit(0)
  else:
    dead("Wrong answer!  You are now a Sphinx McNugget.")
  
def random_room():
  room = randint(0, 3)
  if room == 0:
    bomb_room()
  elif room == 1:
    bear_room()
  elif room == 2:
    ball_room()
  elif room == 3:
    sphinx_room()
  else:
    die('Random number outside of the range of room numbers.  uh oh.')
    
random_room()