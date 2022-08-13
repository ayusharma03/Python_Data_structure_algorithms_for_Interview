class Node:
	def __init__(self, key):
		self.right = None
		self.left = None
		self.key = key

class BinarySearchTree():
	def __init__(self, root = None):
		self.root = root
		
	def get_root(self):
		return self.root
	
# Insert a node 
def insert(self, key):
	if self.root is None:
		self.root = Node(key)
	else:
		self.insertNode(self.root, key)
		
def insertNode(self, this_node, key):
	if self.this_node > key:
		if self.this_node.left is None:
			self.this_node.left = Node(key)
		else:
			self.insertNode(this_node.left, key)
	else:
		if self.this_node.right is None:
			self.this_node.right = Node(key)
		else:
			self.insertNode(this_node.right, key)
			
def find_inorder_successor(self, this_node):
	myval = this_node
	if myval.left  is not None:
		myval = myval.left
	return myval

def find_inorder_predecssor(self, this_node):
	myval = this_node
	if myval.right  is not None:
		myval = myval.right
	return myval
	
def delNode(self, this_node, key):
	if this_node is None:
		reurn this_node
	if key < this_node.key:
		this_node.left =  self.delNode(this_node.left, key)
	if key > this_node.key:
		this_node.right = self.delNode(this_node.right, key)
	else:
		# case 1 or 0 child
		if this_node.right is None:
			temp = this_node.left
			this_node.left = None
			return temp
		elif this_node.left is None:
			temp = this_node.right
			this_node.right = None
			return temp
		# case 2 children
		temp = self.find_inorder_successor(self, this_node.right)
		this_node.key = temp
		this_node.right = self.delNode(this_node.right , temp)
	return this_node
