# '''

# Given an `M × N` integer matrix, return its elements in spiral order.

# Input:

# [
# 	[ 1   2   3   4  5],
# 	[16  17  18  19  6],
# 	[15  24  25  20  7],
# 	[14  23  22  21  8],
# 	[13  12  11  10  9]
# ]

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# '''

# class Solution:
# 	def spiralTraversal(self, mat: List[List[int]]) -> List[int]:
# 		# Write your code here...
# 		ans = []
# 		i = 0
# 		if len(mat) == 0 or (len(mat) and len(mat[0]) == 0):
# 			return ans
# 		er = len(mat)
# 		ec = len(mat[0])
# 		sr = 0
# 		sc = 0
# 		while sr < er and sc < ec:
# 			for i in range(sc,ec):
# 				ans.append(mat[sr][i])
# 			sr += 1
			
# 			for i in range(sr,er):
# 				ans.append(mat[i][ec-1])
# 			ec -= 1
			
# 			if sr < er:
# 				for i in range(ec-1,sc-1,-1):
# 					ans.append(mat[er-1][i])
# 				er -= 1
# 			if sc < ec:
# 				for i in range(er-1,sr-1,-1):
# 					ans.append(mat[i][sc])	
# 				sc += 1
# 		return ans

def spirallyTraverse(matrix, r, c): 
	# code here 
	sr = 0
	sc = 0
	i = 0
	res = []
	prev = matrix[0][0]
	while sr < r and sc < c:
		for i in range(sc,c):
			res.append(matrix[sr][i])
			temp = matrix[sr][i]
			matrix[sr][i] = prev
			prev = temp
		sr += 1
		for i in range(sr,r):
			res.append(matrix[i][c-1])
			temp = matrix[i][c-1]
			matrix[i][c-1] = prev
			prev = temp
		c -= 1
		if sr < r:
			for i in range(c-1,sc-1,-1):
				res.append(matrix[r-1][i])
				temp = matrix[r-1][i]
				matrix[r-1][i] = prev
				prev = temp
			r -= 1
		if sc < c:
			for i in range(r-1,sr-1,-1):
				res.append(matrix[i][sc])
				temp = matrix[i][sc]
				matrix[i][sc] = prev
				prev = temp
			sc += 1
	matrix[0][0] = prev
	print(res)
	print(matrix)
matrix =[[ 1,2,3,4,5],
	[16,17,18,19,6],
	[15,24,25,20,7],
	[14,23,22,21,8],
	[13,12,11,10,9]]
spirallyTraverse(matrix,len(matrix),len(matrix[0]))