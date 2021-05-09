from random import randint

varInt = 10
varString = "loloo"

varString = varString.replace("o", "geg", 2)
print(varString)


def printQ(i):
	if i > 2:
		print(i)
		i /= 2
		printQ(i)
		printQ(i)

def fac(n):
	if n == 1: return 1
	else: return n * fac(n-1)


#printQ(20)
#print(fac(4)) 