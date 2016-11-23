from sys import exit
from random import randint


class Scene(object):
	""" This is the 'template' for each scene.  Write your own enter, and return an entry in the Map for next scene. """

	def enter (self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit (1)


class Death(Scene):

	quips = ["You died.  You kinda suck at this, you know.",
					 "Your mom would be proud...if you were smarter.",
					 "Such a luser!",
					 "I have a small puppy that is better at this!"]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print "Gothon. shoot, dodge, joke?"
		action = raw_input("> ")
		if action == "shoot":
			a = Battle()
			winner = a.combat('hero', 'gothon')
			if winner == 'gothon':
				print "The gothon's lucky shot takes you in the head."
				return 'death'
			elif winner == 'hero':
				print "Your lucky shot hits the gothon in the stones.  He collapses."
				return 'laser_weapon_armory'
		elif action == "dodge":
			print "You attempt to dodge, but it is tough to dodge somebody with the strength and speed of a primate."
			return 'death'
		elif (action == "joke" or action == "cheat"):
			print "Gothons are incredibly weak to bad puns.  He rolls over and convulses, then passes out."
			return 'laser_weapon_armory'
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print "Armory: guess 3 digit code:"
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 1

		while guess != code and guesses < 3:
			print "BZZZZZZT"
			guesses += 1
			guess = raw_input("[keypad]> ")
			if str(guess) == "cheat":
				print "Code: %s" % code

		if guess == code:
			print "success"
			return 'the_bridge'
		else:
			print "Ran out of luck."
			return 'death'

class TheBridge(Scene):

	def enter(self):
		print "Throw or place the bomb?"
		action = raw_input("> ")
		if action == 'throw':
			print "You toss it poorly, dropping down a ventilation shaft, doing minimal damage."
			return 'death'
		if action == 'place' or action == 'cheat':
			print "You sneak past the gothon guards, and place it carefully next to the reactor controller, slipping out."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"

class EscapePod(Scene):

	def enter(self):
		print ("Which pod [1-5]?")
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")

		if guess == good_pod or str(guess) == 'cheat':
			print """You find a working pod!  You dive in and close the door as Gothon solider beams bounce off the hatch. 
You slam the eject button, and shoot off to safety!	"""
			return 'finished'
		else: 
			print "wrong pod."
			return 'death'

class Finished(Scene):

	def enter(self):
		print "You won! Good job."
		return 'finished'

class Battle(Scene):
	def __init__(self):
		hero_health = 20
		enemy_health = 20

	def combat(self, hero_name, enemy_name):
		''' combat function, performs a battle between two opponents.
			inputs: hero name, enemy name.
			returns the winner: hero name or enemy name '''
		hero_health = 20
		enemy_health = 20

		while True:
			damage = randint(1,6)
			print "%s swings and hits for %d damage." % (hero_name, damage)
			enemy_health -= damage
			if enemy_health <= 0:
				return hero_name
			else:
				damage = randint(1,6)
				print "%s swings and hits for %d damage." % (enemy_name, damage)
				hero_health -= damage
				if hero_health <= 0:
					return enemy_name
