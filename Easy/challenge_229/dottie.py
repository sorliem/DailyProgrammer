import math

DOTTIE_NUM = 0.739085133215
TOLERANCE = 0.0000001

def calculateDottie2(n):
    while True: 
        if math.fabs(n - DOTTIE_NUM) < TOLERANCE:
        	return n
        else:
        	n = math.cos(n)

print "Dottie number generator"
num = float(raw_input("Enter a number > "))
result = calculateDottie2(num)

print "result = " + str(result)
