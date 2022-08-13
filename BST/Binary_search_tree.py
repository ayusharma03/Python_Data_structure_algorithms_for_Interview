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
			
