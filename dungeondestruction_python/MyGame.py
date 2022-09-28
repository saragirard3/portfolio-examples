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

party_number = float(0)
p_add = float(0)

# party = {character.capitalize():{ key:[] for key in keys} for character in characters}
party = {}


# c_name = None
# c_race = None
# c_class = None
# c_strength = None
# c_magic = None
# c_dexterity = None
# c_life = None

cls()

print("""
Registrar: Hello everyone. I see you decided to try your hand in this dungeon.
The dungeon only allows up to 5 adventurers per party.

""")
while party_number == 0:
	begin_party = float(input("Tell me, how many of there are you in this party?"))
	if begin_party <= 0:
		print("So you decided to not go into the dungeon. Probably a smart move on your part. Do you want to change your mind with a party number?")
	elif begin_party == 1:
		print("Solo mission, huh? Ok. Well, I guess I'd better hurry and get this headstone order to the sculptor.")
		party_number = begin_party
	elif begin_party == 2:
		print("Double trouble, boil and bubble.")
		party_number = begin_party
	elif begin_party == 3:
		print("Well - three times the charm. Isn't that the saying?")
		party_number = begin_party
	elif begin_party == 4:
		print("This is a nice party. Not too many, but enough for maybe making it back...alive.")
		party_number = begin_party
	elif begin_party == 5:
		print("Nice! Full order of heastones and a sweet payout for me...er...I mean...Good luck and I... *cough*...hope you make it out alive.")
		party_number = begin_party
	elif begin_party >= 6:
		print("That's too many. We only allow a maximum of 5 adventurers per party. Try again.")
	else:
		print("Not sure what you said there. Try again.")

# https://www.programiz.com/python-programming/nested-dictionary
# Basically I want to loop around until all the # of adventurers are entered into the nested dictionary.

def create_characters():
	cls()
	global begin_party
	global p_add
	global party
	print("Registrar:  Let's start with registering each of you individually.")
	while begin_party >=1:
		c_name = input("""
		Adventurer 1, what is your name?

		""")
		party[p_add][name] = c_name
		p_add = p_add + 1
		begin_party = begin_party - 1


create_characters()
print(party)
