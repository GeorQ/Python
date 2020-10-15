valuesOfCoins = [1,2,5,10,20,50,100,200]
def searchMin(T):
	i = 0
	j = len(valuesOfCoins) - 1 
	counter = 0
	while (i < T):
		if (i + valuesOfCoins[j] > T):
			j -= 1
		else:
			i += valuesOfCoins[j]
			counter +=1
	print(counter)

searchMin(4002)
input()

# O(nlogn)
