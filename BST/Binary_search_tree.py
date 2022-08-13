class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_helper(self.root, key)

    def insert_helper(self, this_node, key):
        if this_node.key > key:
            if this_node.left is None:
                this_node.left = Node(key)
            else:
                self.insert_helper(this_node.left, key)

        else:
            if this_node.right is None:
                this_node.right = Node(key)
            else:
                self.insert_helper(this_node.right, key)


    def find_inorder_successor(self, this_node):
        myval = this_node
        while myval.left is not None:
            myval = myval.left
        return myval

    def delete_node(self, this_node, key):
        if this_node is None:
            return this_node
        if key < this_node.key:
            this_node.left = self.delete_node(this_node.left, key)
        elif key > this_node.key:
            this_node.right = self.delete_node(this_node.right, key)
        else:
            # case with no child or 1 child
            if this_node.left is None:
                temp = this_node.right
                this_node = None
                return temp
            elif this_node.right is None:
                temp = this_node.left
                this_node = None
                return temp

            # case with 2 childen
            temp = self.find_inorder_successor(this_node.right)

            this_node.key = temp.key
            this_node.right = self.delete_node(this_node.right, temp.key)
        return this_node
    
    def search(self, this_node, key):
        if this_node is None:
            print('Key not found')
            return False
        elif this_node.key == key:
            print('Key was found')
            return True
        elif key < this_node.key:
            self.search(this_node.left, key)
        else:
            self.search(this_node.right, key)
