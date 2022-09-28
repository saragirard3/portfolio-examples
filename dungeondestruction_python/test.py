from random import randint

party_number = "3"
count3 = float(party_number)
party = {1:{'name':'Sara','race':'Human','class':'Bard','strength':8,'life':15,'magic':2,'dexterity':3}, 2:{'name':'Duane','race':'Elf','class':'Wizard','strength':6,'life':15,'magic':8,'dexterity':3}, 3:{'name':'Liam','race':'Unicorn','class':'Cleric','strength':10,'life':30,'magic':4,'dexterity':3}}

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
	if char_roll >= monst_roll:
		print("You win the bet!")
		break
	else:
		print("Bakeneko wins this round!")
		count3 = count3 - 1
		dic_num = dic_num + 1
		if count3 == 0:
			print('None of you won. You are all mine!')
			dead_bakeneko()
		else:
			Continue

	input("Next player...")
