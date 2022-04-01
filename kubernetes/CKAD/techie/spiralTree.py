'''

Given the root of a binary tree, return the spiral level order traversal of its nodes' values. The solution should consider the binary tree nodes level by level in spiral order, i.e., all nodes present at level 1 should be processed first from left to right, followed by nodes of level 2 from right to left, followed by nodes of level 3 from left to right and so on… In other words, odd levels should be processed from left to right, and even levels should be processed from right to left.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

Output: [1, 3, 2, 4, 5, 6, 8, 7]

'''
res = []
import copy
def ltr(root,level):
	global res
	if root is None:
		return False
	if level == 1:
		# print(root.data,end=" ")
		res.append(root.data)
		return True
	
	elif level > 1:
		left = ltr(root.left,level-1)
		right = ltr(root.right,level-1)
		
		return left or right

def rtl(root,level):
	global res
	if root is None:
		return False
	if level == 1:
		# print(root.data,end=" ")
		res.append(root.data)
		return True
	
	elif level > 1:
		right = rtl(root.right,level-1)
		left = rtl(root.left,level-1)
		
		return right or left
		
	
class Solution:

	'''
	A binary tree node is defined as:

	class Node:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child
	'''

	def findSpiralOrderTraversal(self, root: Node) -> List[int]:
		# Write your code here...
		global res
		if root is None:
			return []
		
		process = True
		level = 1
		while process:
			process = ltr(root,level)
			level += 1
			if process:
				process = rtl(root,level)
				level += 1
		temp = []

		if len(res) != 0:
			temp = copy.copy(res)
			res = []
			return temp
			
		res = []
		return temp

