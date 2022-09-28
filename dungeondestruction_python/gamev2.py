from os import system
from random import randint

gametitle="Dungeon Destruction"
system("mode 200,50")
system("title "+gametitle)

def cls():
	system('cls')

cls()

def Intro():
	print("""

	Welcome Adventurers!
	This dungeon is out of control and we need your help.

	Your choices, skills, and a touch of luck, will influence how well you do.

	We need you all to register before entering the dungeon, we want to be sure you all get your headstones spelled correctly.
	""")
	input('Press ENTER to register...')

Intro()

#for starting the naming structure for the game
party_number = None
party = {}
c_strength = None
c_magic = None
c_dexterity = None
c_life = None

cls()

print("""
Registrar: Hello everyone. I see you decided to try your hand in this dungeon.
The dungeon only allows up to 5 adventurers per party.

""")
while party_number == None:
	begin_party = input("Tell me, how many of there are you in this party?     ")
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
	print("Registrar:  Let's start with registering each of you individually.")
	global party_number
	global party
	p_add = float(party_number)
	c_dict = list()
	dic_num = 0

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

		>
		""")
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

		>
		""")
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

		party[dic_num] = {c_name.capitalize():{'race':c_race,'class':c_class}}
		dic_num = dic_num + 1

create_characters()

def create_character_skill_sheet():
    cls()
    global character_name, character_class,character_race,character_strength,character_magic,character_dexterity,character_life
    print("""
    Now let's determine your character's skills, which you will use throughout the game.
    In this game, your character has four skills:

    - Strength, which you will use in combat or any strength test
    - Dexterity, which you will use in any ability test
    - Magic, which you will use whenever you need to cast a spell or use/inspect a magical item or place
    - Life, which determines your life energy, points will be lost when hurt,
      and whenever Life reaches 0, your character dies.


    Depending on your race and class, you will have a certain point-base already calculated by the game.
    You will shortly be able to increase your skills by rolling a 6-face die.

    Here is your base Character Skills Sheet:
    """)
    character_strength=5
    character_magic=0
    character_dexterity=3
    character_life=10
    if character_race=="Elf":
        character_strength=character_strength+3
        character_magic=character_magic+6
        character_dexterity=character_dexterity+4
        character_life=character_life+2
    elif character_race=="Dwarf":
        character_strength=character_strength+5
        character_life=character_life+4
    if character_class=="Warrior":
        character_strength=character_strength+3
        character_life=character_life+3
    elif character_race=="Wizard":
        character_magic=character_magic+4

    print("""
    Name:"""+character_name+
    """
    Race:"""+character_race+
    """
    Class:"""+character_class+
    """

    Strength:"""+str(character_strength)+
    """
    Dexterity:"""+str(character_dexterity)+
    """
    Magic:"""+str(character_magic)+
    """
    Life:"""+str(character_life)+"""

    """)
    input("Press Enter to apply your skills modifiers")

# create_character_skill_sheet()

print("Registrar:  OK - Here is the information that you registered with:")
count3 = float(party_number)
dic_num = 0

#need to figure out how to print this out neatly but with players names not the dic_num code
while count3 >= 1:
	print(party[dic_num])
	count3 = count3 - 1
	dic_num = dic_num + 1

def hide():
	# party = {character.capitalize():{ key:[] for key in keys} for character in characters}
	# c_name = None
	# c_race = None
	# c_class = None
	# c_strength = None
	# c_magic = None
	# c_dexterity = None
	# c_life = None
	print('hidden stuff for later maybe')
