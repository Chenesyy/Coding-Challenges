import numpy as np

class KadaneAlgorithm:
	def __init__(self, maximum, start, end):
		self.maximum = maximum
		self.start = start
		self.end = end

def kadaneAlgo(arr):
	maximum = 0
	currentMax = 0
	startIndex = -1
	endIndex = -1

	for i, el in enumerate(arr):
		currentMax = currentMax + el
		if currentMax < 0: #everytime current max is less than 0, shift starting index
			startIndex = i+1
		currentMax = max(el, currentMax)
		if currentMax > maximum:
			maximum = currentMax
			endIndex = i

	return KadaneAlgorithm(maximum, startIndex, endIndex)

def maxSumSubRect(matrix):
	L = 0
	R = 0
	currentSum = 0
	maxSum = 0
	maxLeft = -1
	maxRight = -1
	maxUp = -1
	maxDown = -1
	rowLen = len(matrix[0])
	arr = np.zeros(len(matrix))

	while True:
		temp = list()
		for row in matrix:
			temp.append(row[R])

		arr = [sum(i) for i in zip(temp, arr)]

		kadaneResult = kadaneAlgo(arr)
		currentSum = kadaneResult.maximum

		if currentSum > maxSum:
			maxSum = currentSum
			maxLeft = L
			maxRight = R
			maxUp = kadaneResult.start
			maxDown = kadaneResult.end

		R += 1
		if R == rowLen and L+1 == rowLen:
			break
		elif R == rowLen:
			arr = np.zeros(len(matrix))
			L += 1
			R = L

	return maxSum, maxLeft, maxRight, maxUp, maxDown


mat = [
	[2, 1, -3, -4, 5],
	[0, 5, 3, 4, 1],
	[2, -2, -1, 4, -2],
	[-3, 3, 1, 0, 3]
]

print(f"Maximum Sum Submatrix: {maxSumSubRect(mat)[0]}")