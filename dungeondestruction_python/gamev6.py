from os import system
from random import randint

gametitle="Dungeon Destruction"
system("mode 175,30")
system("title "+gametitle)

def cls():
	system('cls')

def next():
	input('Next...')

cls()

def Intro():
	print("""
	*messege board in front of the entrance*

	Welcome Adventurers!
	This dungeon is out of control and we need your help.

	Your choices, skills, and a touch of luck, will influence how well you do.

	We need you all to register before entering the dungeon, we want to be sure you all get your headstones spelled correctly.
	""")

	input('ENTER to register...')

Intro()

#for starting the naming structure for the game
party_number = None
party = {}

cls()

print("""
Registrar:
Hello everyone. I see you decided to try your hand in this dungeon.
The dungeon only allows up to 5 adventurers per party.

""")
while party_number == None:
	begin_party = input("Tell me, how many of there are you in this party?      >")
	if begin_party == "0":
		print("So you decided to not go into the dungeon. Probably a smart move on your part. Do you want to change your mind with a party number?")
	elif begin_party == "1":
		print("Solo mission, huh? Ok. Well, I guess I'd better hurry and get this headstone order to the sculptor.")
		party_number = begin_party
	elif begin_party == "2":
		print("Double trouble, boil and bubble.")
		party_number = begin_party
	elif begin_party == "3":
		print("Well - three times the charm. Isn't that the saying?")
		party_number = begin_party
	elif begin_party == "4":
		print("This is a nice party. Not too many, but enough for maybe making it back...alive.")
		party_number = begin_party
	elif begin_party == "5":
		print("Nice! Full order of heastones and a sweet payout for me...er...I mean...Good luck and I... *cough*...hope you make it out alive.")
		party_number = begin_party
	elif begin_party >= "6":
		print("That's too many. We only allow a maximum of 5 adventurers per party. Try again.")
	else:
		print("Not sure what you said there. Try again.")
		continue

def create_characters():
	cls()
	print("""Registrar:
		Let's start with registering each of you individually.
		""")
	global party_number, party
	p_add = float(party_number)
	c_dict = list()
	dic_num = 1

	while p_add >= 1:
		#get name setup
		c_name = input("""
		Adventurer, what is your name?

		>
		""")
		# c_dict.append(c_name)
		p_add = p_add - 1

		#get race setup
		race = input("""
		Select the corresponding number that represents your race.

		1 - Human
		2 - Fairy
		3 - Elf
		4 - Gnome
		5 - Unicorn

		>""")
		if race =="1":
			c_race = "Human"
		elif race == "2":
			c_race = "Fairy"
		elif race == "3":
			c_race = "Elf"
		elif race == "4":
			c_race = "Gnome"
		elif race == "5":
			c_race = "Unicorn"
		else:
			print('Not a valid choice. We are going to take our best guess - Unicorn')
			c_race = "Unicorn"


		#get class setup
		classtemp = input("""
		Select the corresponding number that represents your class.

		1 - Sorcerer
		2 - Warrior
		3 - Bard
		4 - Cleric
		5 - Rogue

		>""")
		if classtemp =="1":
			c_class = "Sorcerer"
		elif classtemp == "2":
			c_class = "Warrior"
		elif classtemp == "3":
			c_class = "Bard"
		elif classtemp == "4":
			c_class = "Cleric"
		elif classtemp == "5":
			c_class = "Rogue"
		else:
			print('Not a valid choice. Again my best guess is a Cleric.')
			c_class = "Cleric"

		cls()

		#get skills set up
		print("""
			Registrar:
			Now - we need to enter your skills into our biometric tracking.
			That allows us to periodically check on you and see if you died...or um...
			Well, frankly we only needed to check on if people died. I don't know why else we would use it.

			The four skills we track are:
			Strength: for combat
			Dexterity: for abilities use
			Magic: for casting spells
			Life: well to see how long you have before we put you in the box

			Depending on your race and class, you will have a base level for your skills.

			""")
		input("Ok...your base skills...let's see....damn calculator!")

		cls()

		c_strength = 5
		c_magic = 0
		c_dexterity = 3
		c_life = 10

		if c_race=="Fairy":
			c_magic=c_magic+5
			c_life=c_life+3
		elif c_race=="Elf":
			c_dexterity=c_dexterity+3
			c_life=c_life+4
			c_magic=c_magic+2
		elif c_race=="Gnome":
			c_strength=c_strength+5
			c_life=c_life+1
		elif c_race=="Unicorn":
			c_life=c_life+25
			c_magic=c_magic+20
		if c_class=="Sorcerer":
			c_magic=c_magic+5
		elif c_class=="Warrior":
			c_strength=c_strength+5
		elif c_class=="Bard":
			c_dexterity=c_dexterity+5
		elif c_class=="Cleric":
			c_life=c_life+2
		elif c_class=="Rogue":
			c_dexterity=c_dexterity+3
			c_life=c_life+2

		party[dic_num] = {'name':c_name.capitalize(),'race':c_race,'class':c_class,'strength':c_strength,'magic':c_magic,'dexterity':c_dexterity,'life':c_life}
		dic_num = dic_num + 1

		print("""Registrar:
		OK. Well here is your full registration including the skills report that finally calculated.

	    Name:"""+c_name+
	    """
	    Race:"""+c_race+
	    """
	    Class:"""+c_class+
	    """

	    Strength:"""+str(c_strength)+
	    """
	    Dexterity:"""+str(c_dexterity)+
	    """
	    Magic:"""+str(c_magic)+
	    """
	    Life:"""+str(c_life)+"""

	    """)
		input('Ok...NEXT!')
		cls()

create_characters()

print("""
Registrar:
So that looks like that is everyone. Here is everyone's report:

""")
def stats_party():
	global party, party_number
	count3 = float(party_number)
	dic_num = 1

	while count3 >= 1:
		print("""
		Name: """+party[dic_num]['name']+"""
		Race: """+party[dic_num]['race']+"""
		Class: """+party[dic_num]['class']+"""
		Strength: """+str(party[dic_num]['strength'])+"""
		Dexterity: """+str(party[dic_num]['dexterity'])+"""
		Magic: """+str(party[dic_num]['magic'])+"""
		Life: """+str(party[dic_num]['life'])+"""
		""")
		count3 = count3 - 1
		dic_num = dic_num + 1

def stats_party2():
	global party, party_number
	count3 = float(party_number)
	dic_num = 1

	while count3 >= 1:
		print("""
		> """+party[dic_num]['name']+""", Strength: """+str(party[dic_num]['strength'])+""", Dexterity: """+str(party[dic_num]['dexterity'])+""", Magic: """+str(party[dic_num]['magic'])+""", Life: """+str(party[dic_num]['life'])+"""
		""")
		count3 = count3 - 1
		dic_num = dic_num + 1


def stats_life():
	global party, party_number
	count3 = float(party_number)
	dic_num = 1

	while count3 >= 1:
		print("""
		Name: """+party[dic_num]['name']+"""   Life: """+str(party[dic_num]['life'])+"""
		""")
		count3 = count3 - 1
		dic_num = dic_num + 1

stats_party()
next()
cls()

print("""
Registrar:
Ok. Since you are all ready to go. Here are the entrance tickets and your torch. Enjoy your time.
I do hope you survive, but let's be real.

Goodbye Forever!

""")

next()
cls()

def scene_1():
	global party, party_number
	count3 = float(party_number)
	choice = None
	party_dic_rand = randint(1, count3)
	pdr_2 = randint(1, count3)

	while choice is None:
		user_input = input("""
		You have entered the dungeon.

		It is dark and the only light is the torch you just recieved from the Registrar.
		You can see about 15 feet away.
		The stone walls are wet and damp. The air smells like a someone forgot to flush the toilet.
		The corridor is narrow, no wonder only up to five can be in a party. Is """+party[party_dic_rand]['name']+""" actually able to fit with their big butt?

		You come up to a wall.

		You are able to continue to either the left or the right.

		"""+party[pdr_2]['name']+""", what direction do you take the party?

		1 - Turn left
		2 - Turn right

		""")

		if user_input=="1":
			choice = "1"
			scene_2()
		elif user_input=="2":
			choice = "2"
			scene_3()
		else:
			print("What did you say? Be sure to select the corresponding number for the correct direction.")

def scene_2():
	cls()
	global party, party_number
	count3 = float(party_number)
	choice = None
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)

	while choice is None:
		user_input = input("""
		Well the smell hasn't gotten worse, but this hall looks like it might be smaller then the other one.

		As you continue walking, you see light in the distance.
		You notice that there is a bend in the hall.

		You are almost to the end of the hall and you see a door.

		But there is an aweful smell coming from the room.

		"""+party[pdr_1]['name']+""" didn't run ahead so what is that smell.

		The only way to know what the smell is, is to enter the room.

		"""+party[pdr_2]['name']+""", ready to guide your party into the room?

		1 - enter room

		""")
		if user_input == "1":
			choice = "1"
			scene_4()
		else:
			print("Are you having fun taking the smell in from the hall? How about trying again and enter.")

def scene_3():
	cls()
	global party, party_number
	count3 = float(party_number)
	choice = None
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)

	while choice is None:

		user_input = input("""
		They walk a short distance down this hall when all of a sudden....

		*SMASH*

		The ceiling has caved in. The whole hall is covered to the top with debris.

		Do you attempt to dig a path through the debris or return the other way down the hall?

		"""+party[pdr_1]['name']+""", what do you do?

		1 - Dig path through cave in
		2 - Return back to other hall

		""")

		if user_input == "1":
			choice="1"
			scene_18()
		elif user_input == "2":
			choice="2"
			scene_2()

def scene_4():
	cls()
	global party, party_number
	count3 = float(party_number)
	choice = None
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)

	while choice is None:
		user_input = input("""
		The smell was definitely in this room.

		"""+party[pdr_1]['name']+""" takes the torch and lights up the room torches near the door.

		As the room light, you can see bones all over the floor. Something shifts in the corner.

		A low growl comes from the figure and it starts to rise up. It turns around. An ogre.

		"""+party[pdr_2]['name']+""", what do we do? Try to fight or run back?

		1 - Fight!
		2 - Run Away!

		""")
		if user_input == "1":
			choice="1"
			combat_1()
		elif user_input == "2":
			choice="2"
			run_1()

def scene_5():
	cls()
	global party, party_number
	count3 = float(party_number)
	dic_num = 1
	pdr_1 = randint(1, count3)

	print("""
	The ogre is dead. You made it out...mostly alive.""")

	print("""
	Your current life points remaining:	""")
	stats_life()

	print("""
	As you look around the room, """+party[pdr_1]['name']+""" notices a door in the back.
	Finally - a way out.

	""")
	next()
	scene_6()

def scene_6():
		cls()
		global party, party_number
		count3 = float(party_number)
		choice = None
		pdr_1 = randint(1, count3)
		pdr_2 = randint(1, count3)

		while choice is None:
			user_input = input("""
			Finally out of the room, you notice a doorway to the right in the hall.

			"""+party[pdr_1]['name']+""", do you want to lead the team through the door or continue straight down the hall?

			1 - Open the door
			2 - Keep going down the hall

			""")
			if user_input == "1":
				choice="1"
				scene_7()
			elif user_input == "2":
				choice="2"
				scene_8()

def scene_7():
		cls()
		global party, party_number
		count3 = float(party_number)
		choice = None
		pdr_1 = randint(1, count3)
		pdr_2 = randint(1, count3)

		while choice is None:
			user_input = input("""
			"""+party[pdr_1]['name']+""" opens the door.
			As the party walks in, there is a pleasant but misplaced aroma.
			Lined around the room are cushions and pillows. There are little tables with trays of food and wine.

			"""+party[pdr_2]['name']+""" walks to the wine and takes a sip. "It's delicious."

			A figure slowly materializes on the cushion near """+party[pdr_2]['name']+""".

			"I'm glad you like it" said the fully materialized seven tailed bakeneko.

			"You are welcome to more, but each one of you who drink it will be mine forever. Those who stay away, can leave through the door behind me."

			"However I am willing to negotiate. Let's play a game. If you win, everyone can leave. If you lose, you are all mine."

			"Are you willing to test your fate or just leave those who have partook behind?"

			"""+party[pdr_1]['name']+""", do you play to test fate or leave """+party[pdr_2]['name']+""" behind?

			1 - Play and Test fate
			2 - Goodbye friend, but we are leaving without you

			""")
			if user_input == "1":
				choice="1"
				combat_3()
			elif user_input == "2":
				choice="2"
				run_2()

def scene_8():
		cls()
		global party, party_number
		count3 = float(party_number)
		choice = None
		pdr_1 = randint(1, count3)
		pdr_2 = randint(1, count3)

		while choice is None:
			user_input = input("""
			After deciding to skip this doorway, the party doesn't walk far to find another door on the right.
			There is a some light dimly shining through the bottom.

			"""+party[pdr_1]['name']+""", do you want to lead the team through this door or continue straight down the hall?

			1 - Open the door
			2 - Keep going down the hall

			""")
			if user_input == "1":
				choice="1"
				scene_9()
			elif user_input == "2":
				choice="2"
				scene_10()

def scene_9():
		cls()
		global party, party_number
		count3 = float(party_number)
		choice = None
		pdr_1 = randint(1, count3)
		pdr_2 = randint(1, count3)

		while choice is None:
			user_input = input("""
			Being so brave shortly after that fight, the party goes to the door.

			"""+party[pdr_1]['name']+""" opens the door and they find the room is lit fully.

			This room has a beautiful fragrance and warmth to it.

			In the middle of the room there is a box.

			"""+party[pdr_2]['name']+""", do you want to open this box or return to the hall and continue your journey?

			1 - Open the Box
			2 - Continue journey down the hall

			""")
			if user_input == "1":
				choice="1"
				scene_11()
			elif user_input == "2":
				choice="2"
				scene_10()

def scene_10():
	cls()
	global party, party_number
	count3 = float(party_number)
	choice = None
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)


	user_input = input("""
	After walking for a while, the end of the hall is in sight.

	*SMASH*

	What was that sound? """+party[pdr_2]['name']+""" goes ahead to check it out. Right after turning the corner,
	"""+party[pdr_2]['name']+""" gets thrown back into the wall.

	Coming around the corner, a hooded wraith came into view.

	With skeleton hands and face, horns coming out of its head, and in all black. It sees the party and screeches.

	It looks like it's time to fight.

	Next...
	""")

	combat_2()

def scene_11():
	cls()
	global party, party_number
	count3 = float(party_number)
	dic_num = 1
	choice = None
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)

	input("""
	"""+party[pdr_1]['name']+""" goes to the box and opens it.

	Inside there is a HEALTH GROWTH KIT.

	"""+party[pdr_2]['name']+""" reads the kit out loud:

	'THANK YOU FOR YOUR BUSINESS!
	THIS HEALTH GROWTH KIT WILL HELP YOU WITH ALL YOUR DUNGEON SURVIVAL NEEDS.
	IT CONTAINS THE FORMULA TO MAKE THE HEALTH GROWTH POTION AND THE
	MAGICAL SPELL TO READ TO ACTICATE THE FORMULA.

	IN ORDER TO USE THIS POTION AND SPELL, YOU MUST HAVE MAGIC SKILLS OF AT LEAST 5.'

	""")

	while count3 >= 1:
		if party[dic_num]['magic'] < 5:
			print("""
			"""+party[dic_num]['name']+""" doesn't have enough magic skills.
			""")
			count3 = count3-1
			dic_num = dic_num+1
		elif party[dic_num]['magic'] >=5:
			print("""
			"""+party[dic_num]['name']+""" has enough required magic skill.

				They mix and perform the magic.
				Everyone gains 10 Life points.
			""")
			tempcount = float(party_number)
			dic_num = 1
			while tempcount >=1:
				party[dic_num]['life'] = party[dic_num]['life']+10
				tempcount = tempcount -1
				dic_num = dic_num+1
			break

	input("""
	Now the party all regenerated, time to return to the hall and continue our adventure!
	""")
	scene_10()

def scene_12():
	cls()
	global party, party_number
	count3 = float(party_number)
	dic_num = 1
	choice = None
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)

	input("""
	The wraith is dead. As it disintegrates into the air, it drops a adventurer pack.

	"""+party[pdr_1]['name']+""" grabs the pack and opens it.

	Inside there is:
	> ACTIVATED HEALTH POTION ("""+str(count3)+""")
	> ACTIVATED MAGIC POTION ("""+str(count3)+""")
	> ACTIVATED BODY POTION ("""+str(count3)+""")

	The perfect amount for each of us. Its like someone knew we needed that amount.

	The party takes one of each of the activated potions.

	""")

	stats_party2()

	while count3 >= 1:
		party[dic_num]['life'] = party[dic_num]['life']+10
		party[dic_num]['magic'] = party[dic_num]['magic'] + 10
		party[dic_num]['strength'] = party[dic_num]['strength'] + 10
		party[dic_num]['dexterity'] = party[dic_num]['dexterity']+10
		count3 = count3 - 1
		dic_num = dic_num+1

	print('Regenerated Stats:')
	stats_party2()

	input("""
	Now that the party is all regenerated, time to return to the hall and continue our adventure!
	""")
	scene_13()

def scene_13():
	cls()

	input("""
	Feeling regenerated, the party turns down the next hall.

	The hall is just as narrow and just as long as the other ones.
	The only difference is that it's not as wet and there is a bright light at the end of it.

	After the walk, they get to the end of the hall and are greeted to a large gold door.

	No where else to go but in.

	Are you ready?
	""")

	scene_14()

def scene_14():
	print('dragon rooom')

def scene_15():
	cls()
	global party, party_number
	count3 = float(party_number)
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)

	input("""
	"You have won this game. I suppose you are all free to go. I did have a fun time."

	The team walks to the back door and """+party[pdr_1]['name']+""" opens it.

	This next hallway is short and leads to a large room...

	""")
	scene_17()

def scene_17():
	cls()
	global party, party_number
	count3 = float(party_number)
	dic_num = 1
	choice = None
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)

	input("""
	This room is enormous and lined with book covered shelves. In the far corner is a crate.

	"""+party[pdr_1]['name']+""" walks over to the crate and opens it up.

	Inside are multiple viles. """+party[pdr_2]['name']+""" takes them out and reads them.

	Inside there is:
	> ACTIVATED HEALTH POTION ("""+str(count3)+""")
	> ACTIVATED MAGIC POTION ("""+str(count3)+""")
	> ACTIVATED BODY POTION ("""+str(count3)+""")

	The perfect amount for each of us. Its like someone knew we needed that amount.

	The party takes one of each of the activated potions.

	""")

	stats_party2()

	while count3 >= 1:
		party[dic_num]['life'] = party[dic_num]['life']+10
		party[dic_num]['magic'] = party[dic_num]['magic'] + 10
		party[dic_num]['strength'] = party[dic_num]['strength'] + 10
		party[dic_num]['dexterity'] = party[dic_num]['dexterity']+10
		count3 = count3 - 1
		dic_num = dic_num + 1

	print('Regenerated Stats:')
	stats_party2()

	input("""
	Now that the party is all regenerated, time to continue our adventure!
	""")

	scene_13()

def scene_18():
	cls()
	global party, party_number
	count3 = float(party_number)
	pdr_1 = randint(1, count3)
	pdr_2 = randint(1, count3)

	input("""
	"""+pardy[pdr_1]['name']+""" and """+pardy[pdr_2]['name']+""" try to get the debris out of the way.

	Every time the move a little, a lot more falls in it's place.

	Time to give up on the digging this time, let's return down the other hall.

	""")

	scene_2()

#scene 18-25, the right side of the hall through the entry. currently 19 is a turn around spot to the left side.
def scene_19():
	print('bah...trying to do soemthind')

def scene_20():
	print('from 19, room for another attack...need to figure out. need combat 4')

def scene_21():
	print('after combat 4 win. or after going straight from scene 19 hallway that leads to a large room')

def scene_22():
	print('another room entrance before combat number 5')

def scene_23():
	print('after the win leave the room and go into the hall, then a choice to turn left or straight ahead. straigh leads to scene 17 right is scene 24')

def scene_24():
	print(' the long hallway before a deadend, choice to look around the deadend thus moving to scene 25 for secret door and exit. or go back to scene 23 that leads to the room 17')

def scene_25():
	print('finds secret door and shows the exit. Win! go to win scene')

def closet_1():
	print('stuff')

def closet_2():
	print('stuff')

def closet_3():
	print('another stuff')

def closet_4():
	print('finally')

def win():
	print('win scene either way and talk to registrar.')

def combat_1():
	cls()
	global party, party_number
	count3 = float(party_number)
	dic_num = 1
	input("""
	The ogre attacks!

	Get ready and fight!
	""")
	monster = [5,10]

	while monster[1] >= 1:
		try:
			if party[dic_num]['name'] == 'dead':
				count3 = count3-1
				dic_num = dic_num + 1
				continue
		except KeyError:
			print("""
			Registrar:
			Looks like you are all dead, to be expected. Come back in your next life!
			""")
			input('Press ENTER to Close')
			exit()
		input("""
		"""+party[dic_num]['name']+""", it's your turn. Roll to attack!
		""")
		char_roll=randint(1,6)
		print("You attacked with: "+str(char_roll))
		monst_roll=randint(1,6)
		print("The ogre attacks with: "+str(monst_roll))
		if char_roll+party[dic_num]['strength'] >= monst_roll+monster[0]:
			print("You hit the ogre!")
			monster[1]= monster[1]-char_roll
		else:
			print("The ogre hits you!")
			party[dic_num]['life'] = party[dic_num]['life'] - monst_roll
			if party[dic_num]['life'] <= 0:
				print(""" """+party[dic_num]['name']+""", you died. The Registrar will be excited to see your body soon.""")
				party[dic_num]['name'] = 'dead'
				party[dic_num] = party[dic_num] +100
				party_number = party_number - 1
		count3 = count3 - 1
		dic_num = dic_num + 1
		if count3 == 0:
			count3 = float(party_number)
			dic_num = 1

		input("Next attack...")

	input('The ogre stops attacking....')

	scene_5()

def combat_2():
	cls()
	global party, party_number
	count3 = float(party_number)
	dic_num = 1
	input("""
	The wraith attacks!

	Get ready and fight!
	""")
	monster = [8,15]

	while monster[1] >= 1:
		try:
			if party[dic_num]['name'] == 'dead':
				count3 = count3-1
				dic_num = dic_num + 1
				continue
		except KeyError:
			print("""
			Registrar:
			Looks like you are all dead, to be expected. Come back in your next life!
			""")
			input('Press ENTER to Close')
			exit()
		input("""
		"""+party[dic_num]['name']+""", it's your turn. Roll to attack!
		""")
		char_roll=randint(1,6)
		print("You attacked with: "+str(char_roll))
		monst_roll=randint(1,6)
		print("The wraith attacks with: "+str(monst_roll))
		if char_roll+party[dic_num]['magic'] >= monst_roll+monster[0]:
			print("You hit the wraith!")
			monster[1]= monster[1]-char_roll
		else:
			print("The wraith hits you!")
			party[dic_num]['life'] = party[dic_num]['life'] - monst_roll
			if party[dic_num]['life'] <= 0:
				print(""" """+party[dic_num]['name']+""", you died. The Registrar will be excited to see your body soon.""")
				party[dic_num]['name'] = 'dead'
				party[dic_num] = party[dic_num] +100
				party_number = party_number - 1
		count3 = count3 - 1
		dic_num = dic_num + 1
		if count3 == 0:
			count3 = float(party_number)
			dic_num = 1

		input("Next attack...")

	input('The wraith stops its attacks...')

	scene_12()

def combat_3():
	cls()
	global party, party_number
	count3 = float(party_number)
	dic_num = 1
	input("""
	"Nice choice. Better get ready to play. It is a game of chance. Whoever gets the highest number wins.
	I will play each of you individually. If none of you can beat me, then I win. If one of you succeed, you are all free to go."

	"Let's play..."

	""")

	while count3 >= 1:
		input("""
		"""+party[dic_num]['name']+""", it's your turn to roll the dice!
		""")
		char_roll=randint(1,6)
		print("You rolled: "+str(char_roll))
		monst_roll=randint(1,6)
		print("The bakeneko rolled: "+str(monst_roll))
		if monst_roll > char_roll:
			print("Bakeneko wins this round!")
			count3 = count3 - 1
			dic_num = dic_num + 1
			if count3 == 0:
				print('None of you won. You are all mine!')
				dead_bakeneko()
			else:
				input("Next player...")
		else:
			input("You win the bet!")
			scene_15()

def combat_4():
	print('combat from scene 19 choice')

def combat_5():
	print('final combat before dragon room')

def final_combat():
	print('the dragon fight')

def run_1():
	cls()
	global party, party_number
	count3 = float(party_number)
	pdr_1 = randint(1, count3)

	print("""
	You all run to the door that you came in, however, """+party[pdr_1]['name']+""" shut the door behind the party.
	The door is locked.

	Well...this is awkward. Guess there wasn't a choice. We need to fight.
	""")
	next()
	combat_1()

def run_2():
	cls()
	print('this is the giving up friend to the bakeneko')
	global party, party_number
	count3 = float(party_number)
	pdr_1 = randint(1, count3)

	print("""
	You all run to the door that you came in, however, """+party[pdr_1]['name']+""" shut the door behind the party.
	The door is locked.

	Well...this is awkward. Guess there wasn't a choice. We need to fight.
	""")
	next()
	combat_1()

def dead_bakeneko():
	print("""
	"Looks like none of you could win. You are all my personal play things now.

	hahahaha"

	YOU LOSE - TRY AGAIN NEXT TIME.
	""")

	input('Press ENTER to close.')
	exit()

scene_1()


# def scene_4():
# 	cls()
# 	global party, party_number
# 	count3 = float(party_number)
# 	choice = None
# 	pdr_1 = randint(1, count3)
# 	pdr_2 = randint(1, count3)
#
# 	while choice is None:
# 		user_input = input("""
# 		""")
