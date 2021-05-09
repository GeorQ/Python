def BinarySearch(arr, elem, start=0, end=None):

    if end is None:
        end = len(arr) - 1
    if start >= end:
        return False
    sizeOfSec = ((end-start)+1)//3
    mid = start+sizeOfSec
    if elem == arr[mid]: 
        return mid
    if elem < arr[mid]:
        return BinarySearch(arr, elem, start, mid)
    return BinarySearch(arr, elem, mid + 1, end)

arr = [1,2,3,4,5,6,7,8,9]
count = 0

mid = BinarySearch(arr, 6)
print(mid)