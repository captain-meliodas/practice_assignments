def  chProp(root):
	if root is None:
		return 0
	if root.left is None and root.right is None:
		return root.data
	
	left = chProp(root.left)
	right = chProp(root.right)
	
	if left != -float('inf') and right != -float('inf') and root.data == left+right:
		return root.data
	
	return -float('inf')