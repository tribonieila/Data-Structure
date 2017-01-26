def getsum(BIITree, i):
	s = 0
	i = i + 1

	while i > 0:
		s += BIITree[i]
		i -= i & (-i)

	return s

def updatebit(BIITree, n, i, v):
	i += 1
	while i <= n:
		BIITree[i] += v

		i += i & (-i)

def construct(arr, n):
	BIITree = [0]*(n+1)
	for i in range(n):
		updatebit(BIITree, n, i, arr[i])

	return BIITree

freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BIITree = construct(freq, len(freq))

print("Sum of elements in arr[0..5] is " + str(getsum(BIITree, 5)))

freq[3] += 6

updatebit(BIITree, len(freq), 3, 6)

print("Sum of elements in arr[0..5] after update is " + str(getsum(BIITree, 5)))