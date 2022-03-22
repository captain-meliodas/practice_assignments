# https://techiedelight.com/practice/?problem=IsCompleteBinaryTree

'''

Given the root of a binary tree, check if it is a complete binary tree or not. A complete binary tree is a binary tree in which every level, except possibly the last, is filled, and all nodes are as far left as possible.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  / \	  /
	 /	 \	 /
	4	 5	6

Output: True

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /		 /	 \
	4		5	  6

Output: False

'''

class Solution:

	'''
	A binary tree node is defined as:

	class Node:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child
	'''

	def isComplete(self, root: Node) -> bool:
		# Write your code here...
		if root is None:
			return True
		flag = False
		queue = []
		queue.append(root)
		while len(queue) != 0:
			temp = queue.pop(0)
			if temp.left:
				if flag == True:
					return False
				
				queue.append(temp.left)
			else:
				flag = True
			
			if temp.right:
				if flag == True:
					return False
				
				queue.append(temp.right)
			else:
				flag = True
				
		return True

