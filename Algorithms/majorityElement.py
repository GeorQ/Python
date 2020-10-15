def search(A):
	A.sort()
	value = A[0];
	counter = 1;
	for i in range(1, len(A)):
	    if (A[i] == value):
	        counter += 1
	        if (counter > len(A) / 2):
	            return True
	    else:
	        value = A[i]
	        counter = 1
	return False
	
a = search([1,1,1,2,1,6,1,2,3,4,1])
print(a)
input()

# O(nlogn)