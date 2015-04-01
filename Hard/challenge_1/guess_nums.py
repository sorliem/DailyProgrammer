#!/usr/bin/python3
import random as rand

def guess():
	print("Welcome to the guessing game.\nThink of a number bettween 0 and 100 and I'll try to guess it. Ready?\n\n")
	guessRange = []
	for i in range(101):
		guessRange.append(i)
	while (True):
		guess = rand.randrange(len(guessRange)) + guessRange[0];
		print("Guess: " + str(guess))
		ans = input("(h)igh or (l)ow? ")
		if (ans == "l"):
			guessRange = chopLower(guess)
		elif (ans == "h"):
			guessRange = chopUpper(guess)
		else:
			print("(borg-beep-boop) yay I found it!")

def chopUpper(pt):
	pass #todo

def chopLower(pt):
	pass #todo

if __name__ == "__main__":
	guess()