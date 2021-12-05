from random import randrange

#list of play options
t = ["Rock", "Paper", "Scissors"]

#assign random play to PC
computer = t[randrange(0,2)]

#set the player to False
player = False

while player == False:
#set player true
	player = input("Rock, Paper, Scissors?")
	if player == computer:
		print("Tie!")
	elif player == "Rock":
		if computer == "Paper":
			print("you lose!", computer, "covers", player)
		else:
			
			print("you win!", player, "smashes", computer)
			
	elif player == "Scissors":
		if computer == "Rock":
			print("you lose!", computer, "smashes", player)
		else:
			
			print("you win!", player, "cut", computer)
	elif player == "Paper":
		if computer == "Scissors":
			print("you lose!", computer, "cuts", player)
		else:
			
			print("you win!", player, "covers", computer)
	else:
		
		print("not a valid option check spelling")
	
#player was set to True, but we want it to be False so the loop continues
player = False

computer = t[randrange(0,2)]
