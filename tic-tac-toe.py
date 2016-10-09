#Text-Based Tic Tac Toe (Computer Makes Moves Randomly) 
#Using https://repl.it/languages/python3
#Author: Robert Beckett
from random import randint

#This function prints the board. (View section)

def PrintBoard():
	print(a1, a2, a3)
	print(b1, b2, b3)
	print(c1, c2, c3)
	print("\n")
	
#This function checks whether either x or o has 3 in a row for a given set of 3 variables. (Model Section)
def WinTest(wtone, wttwo, wtthree):
	if wtone == " X " and wttwo == " X " and wtthree == " X ":
		PrintBoard()
		print("You win!")
		quit()
	if wtone == " O " and wttwo == " O " and wtthree == " O ":
		PrintBoard()
		print("Computer Wins!")
		quit()

#This function uses WinTest to check every possible win on the board. (Model Section)
def HasSomeoneWon():
	WinTest(a1, a2, a3) 
	WinTest(b1, b2, b3)
	WinTest(c1, c2, c3)
	WinTest(a1, b1, c1)
	WinTest(a2, b2, c2)
	WinTest(a3, b3, c3)
	WinTest(a1, b2, c3)
	WinTest(a3, b2, c1)
	if a1 != " - " and a2 != " - " and a3 != " - " and b1 != " - " and b2 != " - " and b3 != " - " and c1 != " - " and c2 != " - " and c3 != " - ":
		print("Cat's Game!")
		PrintBoard()
		quit()
		
def ValidateAndPlay(turn, XorO): #Check if the cell is empty. If so play and return "False". Otherwise, return, "True." (Model Section)
	global a1, a2, a3, b1, b2, b3, c1, c2, c3
	if turn == str('a1') and a1 == " - ": #validate that cell is empty
		a1 = XorO
		return False
	elif turn == str('a2') and a2 == " - ":
		a2 = XorO
		return False
	elif turn == str('a3') and a3 == " - ":
		a3 = XorO
		return False
	elif turn == str('b1') and b1 == " - ":
		b1 = XorO
		return False
	elif turn == str('b2') and b2 == " - ":
		b2 = XorO
		return False
	elif turn == str('b3') and b3 == " - ":
		b3 = XorO
		return False
	elif turn == str('c1') and c1 == " - ":
		c1 = XorO
		return False
	elif turn == str('c2') and c2 == " - ":
		c2 = XorO
		return False
	elif turn == str('c3') and c3 == " - ":
		c3 = XorO
		return False
	else:
		return True

def HumanTurn(): #input a cell from player (Control Section)
	playing = True
	while playing == True:
		global a1, a2, a3, b1, b2, b3, c1, c2, c3
		print ('Please enter an unoccupied space using these codes:')
		print ("\n")
		print ('a1, a2, a3')
		print ('b1, b2, b3')
		print ('c1, c2, c3')
		turn = input()
		if ValidateAndPlay(turn, " X ") == False:
			playing = False
		
#This function has a while loop that generates a random number between 1 and 9, checks if the corresponding spot on the board is empty, then plays if the spots available. If it's not available, it generates another random number and tries again. (Model Section)

def ComputerTurn(): 
	playing = True
	while playing == True:
		global a1, a2, a3, b1, b2, b3, c1, c2, c3
		randturn = randint(1,9)
		if randturn == 1 and ValidateAndPlay("a1", " O ") == False:
			playing = False
		elif randturn == 2 and ValidateAndPlay("a2", " O ") == False:
			playing = False
		elif randturn == 3 and ValidateAndPlay("a3", " O ") == False:
			playing = False
		elif randturn == 4 and ValidateAndPlay("b1", " O ") == False:
			playing = False
		elif randturn == 5 and ValidateAndPlay("b2", " O ") == False:
			playing = False
		elif randturn == 6 and ValidateAndPlay("b3", " O ") == False:
			playing = False
		elif randturn == 7 and ValidateAndPlay("c1", " O ") == False:
			playing = False
		elif randturn == 8 and ValidateAndPlay("c2", " O ") == False:
			playing = False
		elif randturn == 9 and ValidateAndPlay("c3", " O ") == False:
			playing = False

#This introduces variables used to see if someone has won.
	
#This sets up the variables for the board at the beginng of a game.
def gameinit():
	global a1, a2, a3, b1, b2, b3, c1, c2, c3
	a1 = " - "
	a2 = " - "
	a3 = " - "
	b1 = " - "
	b2 = " - "
	b3 = " - "
	c1 = " - "
	c2 = " - "
	c3 = " - "

def main():
	gameinit()
	print("Welcome to Tic Tac Toe!")
	
	#In this section, it randomly chooses the first player.
	#The computer also always assigns O's to the computer and X's to the human.
	#Eventually it'll be nice and ask if the user wants to go first
	#or play X's or O's.
	
	#pick 1 or 2. This is the start number.
	i = randint(1,2) 
	while i < 15:
		PrintBoard()
		#Even numbers = user goes.
		if i % 2 == 0: #
			HumanTurn()
			HasSomeoneWon()
		#Otherwise= computer goes.
		else:
			ComputerTurn()
			HasSomeoneWon()
		i += 1
		
main()
