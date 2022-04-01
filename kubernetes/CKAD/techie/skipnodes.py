'''

Given a singly-linked list of integers and two positive numbers, m and n, delete every n nodes after skipping m nodes.

Input: List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> 9 —> 10 —> None, m = 1, n = 3
Output: 1 —> 5 —> 9 —> None

Input: List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> 9 —> 10 —> None, m = 2, n = 2
Output: 1 —> 2 —> 5 —> 6 —> 9 —> 10 —> None

Input: List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> None, m = 4, n = 6
Output: 1 —> 2 —> 3 —> 4 —> None

Input: List: 1 —> 2 —> 3 —> None, m = 4, n = 2
Output: 1 —> 2 —> 3 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def deleteNodes(self, head: Node, m: int, n: int) -> Node:
		# Write your code here...
		if head is None or head.next is None:
			return head
		
		curr = head
		prev = None
		
		#skip m nodes
		for i in range(1,m+1):
			prev = curr
			curr = curr.next
			if curr is None:
				return head
		#delete n nodes
		for i in range(1,n+1):
			if curr:
				curr = curr.next
		
		prev.next = curr
		self.deleteNodes(curr,m,n)
		return head
			

