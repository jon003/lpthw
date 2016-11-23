from sys import exit
from random import randint

class Scene(object):

	def enter (self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit (1)


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		pass

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		current_scene.enter()

class Death(Scene):

	quips = ["You died.  You kinda suck at this.",
					 "Your mom would be proud...if she were smarter.",
					 "Suck a luser.",
					 "I have a small puppy that is better at this."]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print "Gothon. shoot, dodge, joke?"
		action = raw_input("> ")
		if action == "shoot":
			print "text"
			return 'death'
		elif action == "dodge":
			print "text"
			return 'death'
		elif action == "joke":
			print "text"
			return 'laser_weapon_armory'
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print "Armory: guess 3 digit code:"
		#code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		code = '999'
		guess = raw_input("[keypad]> ")
		guesses = 1

		while guess != code and guesses < 3:
			print "BZZZZZZT"
			guesses += 1
			guess = raw_input("[keypad]> ")

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
			print "you toss it poorly."
			return 'death'
		if action == 'place':
			print "you place it gently"
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"

class EscapePod(Scene):

	def enter(self):
		print ("Which pod [1-5]?")
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")

		if int(guess) != good_pod:
			print "wrong pod."
			return 'death'
		else: 
			print "working pod!"
			return 'finished'

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

''' use this for debugging a battle
a = Battle()
print a.combat('jon', 'gothon')
'''

class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

''' study drills

1. nah
2. because your first test is outside the while loop, then you loop 10 times for a total of 11
3. 


We return the room, which is the variable name we look up in Map.scenes dictionary to find the right function to call 
for the next room.

for instance, we're in the bridge, and it returns escape_pod on successful action.

This returns back to the Engine.play() function in the Engine class, specifically the while loop:

while current_scene != last_scene:
	next_scene_name = current_scene.enter()
	current_scene = self.scene_map.next_scene(next_scene_name)

See how next_scene_name is now getting the value returned from current.scene.enter()?  That is the return value.
On the next line, you see the current scene is then set to the dictionary lookup value of self.scene_map.next_scene(),
which is just a quick lookup function of the scene name from the Map.

4. done.
5. done!  see battle class, above.
6. done. 

'''