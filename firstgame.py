from time import sleep
from sys import exit
import random
p = "> "
g = 0
spider_dead = False
snake_dead = False
dragon_dead = False
hint_found = False
key_found = False
sword_found = False
small_found = False
large_found = False
pile_looted = False
axe_broken = False
rock = False
snake_found = False
treasure_found = False
dragon_health = 100

def win():
	print '''
	You have escaped the castle victorious!
	You looted %d gold pieces in your adventure
	and have slain a fearsome dragon.
	
	Thank you for playing!
	
	''' % g
	sleep(3)
	print '''
	Programmed and written by: Casey Ferguson
	
	'''
	sleep(3)
	print '''
	Special thanks to Zed Shaw for teaching me Python "the hard way"
	
	'''
	sleep(3)
	print '''
	Copyright 2014 - Cesium Knight Games
	All rights reserved.
	
	'''
	sleep(3)
	print '''
	Reproduction permitted with permission from Casey Ferguson
	caseyjferguson@gmail.com
	'''
	exit(0)
	

def idk():
	print "I don't know what you mean."

#dead
def dead(cause):
	print cause,"You have died."
	exit(0)
#gold
def gold():
	global g
	if g == 0:
		g = "no"
	print "You have %r gold in your coinpouch." % g
	if g == "no":
		g = 0
		
#hint
def hint():
	if hint_found:
		print '''
		The sage told you this in the hint room:
		Move like a bishop,
		then like a knight
		to find the key
		to your heart's delight.
		'''
	else:
		print "What hint?"
		
#small_chest_room
def small_chest_room():
	global small_found
	global g
	print '''
	This room contains a small chest on the western wall.
	It also has doors on the north and south walls.
	'''
	dec = raw_input(p)
	if "open" in dec and not small_found:
		print "You open the chest and find 25 gold pieces."
		g += 25
		small_found = True
	elif "open" in dec and small_found:
		print "This chest is empty."
	elif "north" in dec:
		zero_two_room()
	elif "south" in dec:
		spider_room("north")
	elif dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	else:
		idk()
	
	small_chest_room()

#zero_two_room
def zero_two_room():
	print '''
	The gilded walls in this room betray the gloomy nature of the rest of the castle.
	There's a door on the north wall, one on the east wall, and one on the south.
	'''
	dec = raw_input(p)
	if "north" in dec:
		axe_room("south")
	elif "south" in dec:
		small_chest_room()
	elif "east" in dec:
		snake_room()
	elif dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	else:
		idk()
	zero_two_room()
	
#axe_room
def axe_room(side):
	global axe_broken
	global rock
	if axe_broken:
		axe = "is broken, and hangs motionless"
	else:
		axe = "sways back and forth like a pendulum"
	print '''
	This room is well lit, but there is an axe hanging from the ceiling.
	It %s.
	There's a door on the north wall and a door on the south wall.
	''' % (axe)
	dec = raw_input(p)
	if "rock" in dec:
		print "You find a rock on the ground"
		rock = True
	elif "throw" in dec and rock and not axe_broken:
		print "You throw the rock at the mechanism."
		print "It breaks!"
		axe_broken = True
		rock = False
	elif "throw" in dec and rock and axe_broken:
		print "You throw the rock at the mechanism."
		print "It pings off with a metallic ring."
	elif "throw" in dec and not rock:
		print "You have nothing to throw!"
	elif "axe" in dec and not axe_broken:
		dead("You got too close to the swinging axe!")
	elif "south" in dec and side == "north" and not axe_broken:
		dead("You walked past a swinging axe. What are you on?")
	elif "north" in dec and side == "south" and not axe_broken:
		dead("You walked past a swinging axe. What are you on?")
	elif "north" in dec:
		zero_four_room()
	elif "south" in dec:
		zero_two_room()
	elif dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	else:
		idk()
	axe_room(side)
	
		
#zero_four_room
def zero_four_room():
	print "This room is a sweeping hallway with doors on the east and south walls."
	dec = raw_input(p)
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "south" in dec:
		axe_room("north")
	elif "east" in dec:
		one_four_room()
	else:
		idk()
	zero_four_room()

#hint_room
def hint_room():
	global g
	global hint_found
	print '''
	This room contains only a counter and a barstool.
	At the barstool, an old man sits.
	'''
	dec = raw_input(p)
	
	if "talk" in dec or "chat" in dec or "speak" in dec:
		print '''
		Hello there, adventurer!
		I have a clue.
		Bring me some gold,
		and I'll share with you!
		'''
	elif ("buy" in dec or "trade" in dec) and g >= 25 and not hint_found:
		print '''
		I can certainly share my hint! Thanks for your patronage!
		
		First like a bishop,
		then like a knight
		will give you the key
		to your heart's delight!
		'''
		hint_found = True
		g -= 25
	elif ("buy" in dec or "trade" in dec) and g >= 25:
		print "I've already shared my hint"
	elif "buy" in dec or "trade" in dec:
		print "You haven't enough gold!"
		print "*You have %d gold of a required 25.*" % g
	elif dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "south" in dec:
		foyer()
	elif "east" in dec:
		two_one_room()
	elif "man" in dec:
		print "The man is blind and gray haired, with a blindfold over his eyes."
	else:
		idk()
	hint_room()
		
#snake_room
def snake_room():
	global snake_dead
	global pile_looted
	global g
	global snake_found
	if pile_looted and snake_dead:
		corner = "there lies a dead snake"
	elif not pile_looted and snake_dead:
		corner = "there lies a dead snake on a pile of gold"
	elif not pile_looted and not snake_found:
		corner = "you see a shimmer"
	elif not pile_looted and not snake_dead and snake_found:
		corner = "you see a snake resting atop a modest pile of gold"
	print '''
	This room is low lit, and smells of swamp.
	It's very humid.
	In the eastern corner of the room, %s.
	There's a door to the west.
	''' % corner
	
	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "shimmer" in dec:
		print "You examine the shimmer."
		print "It appears to be a moderate pile of gold pieces."
		print "As you approach, a large snake slithers it's way from the pile."
		snake_found = True
	elif ("take" in dec or "loot" in dec) and not snake_dead:
		dead("The snake lunges for your throat and strangles you.")
	elif "grab" in dec or "stomp" in dec or "kill" in dec or ("crush" in dec and rock):
		hit = random.randrange(1,100)
		if hit > 30:
			print "You successfully %s for %d damage." % (dec, hit)
			snake_dead = True
		else:
			dead("You attempt to %s and the snake dodges you and strikes." % dec)
	elif "run" in dec or "flee" in dec:
		zero_two_room()
	elif ("take" in dec or "loot" in dec) and snake_dead:
		print "You find 50 gold in the pile."
		g += 50
		pile_looted = True
	elif "west" in dec:
		zero_two_room()
	else:
		idk()
	snake_room()
	
#large_chest_room
def large_chest_room():
	global sword_found
	global g
	print '''
	This room contains only a large gilded chest and velvet tapestry.
	The chest appears unlocked.
	There is a door to the north, and one to the east.
	'''
	
	dec = raw_input(p)
	
	if "open" in dec:
		print '''
		You open the chest.
		Inside there lies a glowing longsword
		and a large pile of gold pieces.
		'''
		sword_found = True
		g += 100
	elif "chest" in dec:
		print "The chest has inscriptions of a firebreathing dragon on it's gilded lid."
	elif dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "north" in dec:
		one_four_room()
	elif "east" in dec and not key_found:
		print "This door is locked."
	elif "east" in dec:
		print "You used the key."
		arrow_room()
	else:
		idk()
	large_chest_room()
		
#one_four_room
def one_four_room():
	print '''
	This corridor has three doors, 
	on the north, west, and south walls.
	'''
	
	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "north" in dec and not key_found:
		print "This door is locked."
	elif "north" in dec:
		treasure_room()
	elif "south" in dec:
		large_chest_room()
	elif "west" in dec:
		zero_four_room()
	else:
		idk()
	one_four_room()
		
#treasure_room
def treasure_room():
	global g
	global treasure_found
	if treasure_found:
		found = "This room once held the castles treasure."
	else:
		found = "This room is filled with many gems and golden trinkets."
	print '''
	Congratulations!
	You have reached your goal!
	%s
	''' % found
	
	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		print "Why do you need a hint now?"
	elif "take" in dec or "loot" in dec:
		print "You %s." % dec
		g += 400
		treasure_found = True
	elif "south" in dec and not key_found:
		print "This door is locked."
	elif "south" in dec:
		one_four_room()
	elif "east" in dec:
		dragon_room()
	elif "treasure" in dec:
		print "The treasure appears to be worth about 400 gold pieces."
	elif "gem" in dec:
		print "There appears to be several rubies and emeralds in the pile."
	else:
		idk()
	treasure_room()
	
#two_one_room
def two_one_room():
	print '''
	This is a sweeping corridor.
	There are doors on the north and west walls.
	'''

	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "north" in dec:
		two_two_room()
	elif "west" in dec:
		hint_room()
	else:
		idk()
	two_one_room()

#two_two_room
def two_two_room():
	print '''
	This is a straight and empty corridor,
	save for the tapestry on the walls.
	'''
	
	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "tapestry" in dec:
		print "The tapestry depicts a large red dragon sleeping in a room too small for it."
	elif "north" in dec:
		arrow_room()
	elif "south" in dec:
		two_one_room()
	else:
		idk()
	two_two_room()

#arrow_room
def arrow_room():
	print '''
	This room is large and dark.
	In the center of the room on the floor
	there is a glowing white arrow facing the eastern door.
	There are doors on every wall.
	'''
	
	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "arrow" in dec:
		print '''
		The arrow glows in the dark room,
		as if by magic. It points to the
		eastern door.
		'''
	elif "north" in dec:
		two_four_room()
	elif "west" in dec and not key_found:
		print "This door is locked."
	elif "west" in dec:
		large_chest_room()
	elif "south" in dec:
		two_two_room()
	elif "east" in dec:
		pungee_room()
	else:
		idk()
	arrow_room()
		
#two_four_room
def two_four_room():
	print '''
	This is a straight hallway, 
	with a door on the east wall.
	'''
	
	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "east" in dec:
		key_room()
	elif "north" in dec:
		dragon_room()
	elif "south" in dec:
		arrow_room()
	else:
		idk()
	two_four_room()
	
#dragon_room
def dragon_room():
	global dragon_health
	global dragon_dead
	if dragon_dead:
		dragon = "dead"
		lived = " "
	else:
		dragon = "red"
		lived = " has "
	print '''
	Before you lies a large %s dragon.
	It appears to be much too large to have entered this room.
	It%slikely lived here much of its life in solitude.
	The room smells of smoke and charred flesh.
	There are bones strewn around the room.
	''' % (dragon, lived)
	
	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif ("attack" in dec or "kill" in dec) and sword_found and not dragon_dead:
		print "You take a swing at the dragon with your sword."
		hit = random.randrange(1,100)
		sleep(1)
		if hit >= 30:
			print "Your blow lands on the dragon."
		else:
			print "You fail to land a strike."
		dragon_health -= hit
		if dragon_health <= 0:
			dragon_dead = True
	elif "dragon":
		print "It is large and red, with scales the size of many shields."
	else:
		idk()
	
	if dragon_dead == False:
		print '''
		The dragon notices your presence and attacks.
		'''
	
		dec = raw_input(p)
		hit = random.randrange(1,100)
		if hit >= 80:
			attack = "fire"
		else:
			attack = "his claws"
		if "dodge" in dec:
			print "The dragon attacks with %s and you dodge the attack." % attack
			dragon_room()
		elif "block" in dec and attack == "claws" and sword_found == true:
			print "The dragon attacks with his claws and you successfully block with your sword."
			dragon_room()
		elif "block" in dec and attack == "fire":
			dead("The dragon attacks with fire and your block is ineffective. You are charred.")
		elif "block" in dec:
			dead("The dragon attacks with %s and you have nothing to block with." % attack)
		else:
			dead("The dragon attacks with %s." % attack)
	else:
		print '''
		Congratulations, the dragon has been defeated.
		There are doors on every wall.
		The north door has a barred slit that daylight shows through.
		'''
		
		dec = raw_input(p)
		
		if dec == "gold":
			gold()
		elif dec == "hint":
			hint()
		elif "east" in dec:
			bottomless_pit_room()
		elif "north" in dec:
			win()
		elif "south" in dec:
			two_four_room()
		elif "west" in dec:
			treasure_room()
		else:
			idk()
		dragon_room()
		
#pungee_room
def pungee_room():
	dead("You step into a very dark room, and as you take your step in, the floor gives way. You are impaled on pungee spikes.")

#key_room
def key_room():
	global key_found
	print '''
	A brightly colored room lies before you.
	There are doors on the west wall and south wall.
	'''
	if key_found:
		print '''
		A golden pedestal where a key once laid sits in the middle of the room.
		'''
	else:
		print '''
		A key is illuminated on a golden pedestal in the center of the room.
		'''
	
	dec = raw_input(p)
	
	if dec == "gold":
		gold()
	elif dec == "hint":
		hint()
	elif "take" in dec or "loot" in dec and not key_found:
		key_found = True
		print "You have retrieved the key."
	elif "key" in dec:
		print "The key is solid gold with a ruby serpent embedded in the handle."
	elif "south" in dec:
		pungee_room()
	elif "west" in dec:
		two_four_room()
	else:
		idk()
	key_room()
	
#bottomless_pit_room
def bottomless_pit_room():
	print "You step into an abyss and begin falling."
	fallcount = random.randrange(10,40)
	for i in range(1, fallcount):
		print "Still falling..."
		sleep(2)
	dead("You land with a splat on a hard bedrock surface.")
def start():
	print '''
	Welcome to the castle of wonder!
	Deep within, there are secrets to behold.
	One room holds a treasure so lucrative,
	you will never need for anything again.
	'''
	foyer()
	
def foyer():
	print '''
	You are in a well lit foyer.
	There are torches in ever corner of this large room,
	and there are doors on every one of the four walls.
	
	The exit is on the south wall, if you wish to leave.
	
	Which door do you take?
	'''
	
	door = raw_input(p)
	
	if "north" in door:
		print "You chose the north door."
		hint_room()
	elif "east" in door:
		print "You chose the east door."
		mamba_room()
	elif "west" in door:
		print "You chose the west door."
		spider_room("foyer")
	elif "south" in door and dragon_dead:
		win()
	elif "south" in door:
		print "You are now leaving the castle of wonder."
		print "Have a good day!"
		exit(0)
	elif door == "hint":
		hint()
	elif door == "gold":
		gold()
	else:
		idk()
	foyer()
		
def mamba_room():
	dead("As you step into the room, you are immediately bitten by a deadly black mamba.")
	
def spider_room(entry):
	global spider_dead
	spider = "You hear the skittering of a large spider approaching you"
	if spider_dead == False:
		spider = "You hear the skittering of a large spider approaching you"
	else:
		spider = "A large spider lays dead on the floor"
	print '''
	You are in a dark room.
	%s.
	There are doors to the north and east.
	What do you do?
	''' % spider
	choice = raw_input(p)
	if choice == "flee" and entry == "foyer":
		foyer()
	elif choice == "flee" and entry == "chest":
		small_chest_room()
	elif "stomp" in choice or "step" in choice:
		print "You %s and kill it." % choice
		spider_dead = True
	elif "kill" in choice or "squish" in choice or "smash" in choice or "crush" in choice:
		print "You %s." % choice
		spider_dead = True
	elif not spider_dead:
		dead("The spider climbs on your leg and injects is venom.")
	elif "north" in choice:
		small_chest_room()
	elif "east" in choice:
		foyer()
	elif choice == "gold":
		gold()
	elif choice == "hint":
		hint()
	else:
		print "I don't know what you mean"
	spider_room("room")
		
start()