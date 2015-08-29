#!/usr/bin/python

from sys import argv
import random
import math1

def importWords(file_handle):
	pass

def checkInBounds(word, startX, startY, direction):
	pass

def placeWord(word, x, y, direction):
	pass

def buildSnake(words):
	lastX = 0
	lastY = 0
	for x in words:
		direction = math.floor(random.random() * 4)
		if direction == 0:
			if (checkInBounds(x, lastX, lastY, direction))
			good = checkInBounds()





# if __name__ == "__main__":
script, file_handle = argv
fr = open(file_handle)
words = fr.read().split(' ')
print "list of words " + str(words)
Matrix = [[0 for x in range(40)] for x in range(40)]
