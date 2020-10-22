A = [5,7,4,3,6,8,3,6,7,2]
counter = 0
for i in range(1, len(A)):
	counter += 1
	key = A[i]
	j = i - 1
	while j >= 0 and A[j] > key:
		A[j + 1] = A[j]
		j -= 1 
	A[j + 1] = key

print(A)
print(counter)