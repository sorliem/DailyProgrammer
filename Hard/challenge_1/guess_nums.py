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
		ans = input("(h)igh or (l)ow or (c)orrect? ")
		if (ans == "l"):
			guessRange = chopLower(guess, guessRange)
		elif (ans == "h"):
			guessRange = chopUpper(guess, guessRange)
		else:
			print("(borg-beep-boop) yay I found it!")
			break;

def chopUpper(pt, rng):
	"""From the pt in the range given, return rng[0:i]"""
	for i in range(len(rng)):
		if rng[i] == pt:
			return rng[0:i]

def chopLower(pt, rng):
	"""From index 0 to the range given, return rng[i+1:len(rng)]"""
	for i in range(len(rng)):
		if rng[i] == pt:
			return rng[i+1:len(rng)]

if __name__ == "__main__":
	guess()