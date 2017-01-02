# made with python 3

skillLevel = "p"
missle = 0
play = True

# None -> Strings
# introduces the player to the game
# def intro(): 
#tests
# template
def intro():
	print("Hello and welcome to one of the more unpleasant gameing")
	print("experiences you will ever have, prepare to be underwelmed")
	print("skill level. Sorry there is only novice for new.")
	skillLevel = input()
	skill(skillLevel)

# string -> string
# determines the skill level
# def skill(skillLevel):
#Test
# Template
def skill(s):
	if s == "novice" :
		missle = 5
		print("hello")
	else: print("Why are you here")
intro()


