'''

Given a singly-linked list of integers, construct a complete binary tree out of it. Assume that the order of elements present in the linked list is the same as that in the complete tree's array representation. i.e., for a tree node at position i (position starting from 1) in the linked list, the left child is present at the position 2×i, and the right child is present at the position 2×i + 1.

Input: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> None
Output:

			1
		  /   \
		 /	   \
		2		3
	   / \	   /
	  /	  \	  /
	 4	   5 6

'''
def insertlevelorder(arr,root,index,n):
	if index < n:
		temp = TreeNode(arr[index])
		root = temp
		root.left = insertlevelorder(arr,root.left,2*index+1,n)
		root.right = insertlevelorder(arr,root.right,2*index+2,n)
	
	return root
class Solution:

	'''
	A binary tree node is defined as:

	class TreeNode:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child


	A singly-linked list node is defined as:

	class ListNode:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''
		

	def convertListToBinaryTree(self, head: ListNode) -> TreeNode:
		# Write your code here...
		temp = []
		thead = head
		root = None
		if thead:
			while thead.next != None:
				temp.append(thead.data)
				thead = thead.next
			temp.append(thead.data)
			root = None
			n = len(temp)
			index = 0
			root = insertlevelorder(temp,root,index,n)

		return root

