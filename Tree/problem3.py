# Check if a binary tree is a binary search tree (BST).

class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None   
        self.right = None  


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)  # Create the root node

    def insert_left(self, parent, value):
        """ Insert a node to the left of the given parent node """
        parent.left = Node(value)

    def insert_right(self, parent, value):
        """ Insert a node to the right of the given parent node """
        parent.right = Node(value)

    def is_bst(self, node, min_val=float('-inf'), max_val=float('inf')):
        """ Check if the tree is a binary search tree (BST) """
        if node is None:
            return True
        
        # Node's value must be within the allowed range
        if node.value <= min_val or node.value >= max_val:
            return False

        # Recursively check the left and right subtrees
        return (self.is_bst(node.left, min_val, node.value) and
                self.is_bst(node.right, node.value, max_val))



tree = BinaryTree(10)  # Root node with value 10

# Inserting nodes
tree.insert_left(tree.root, 5)
tree.insert_right(tree.root, 15)

tree.insert_left(tree.root.left, 3)
tree.insert_right(tree.root.left, 7)

tree.insert_left(tree.root.right, 12)
tree.insert_right(tree.root.right, 18)

# Check if the tree is a BST
if tree.is_bst(tree.root):
    print("The tree is a Binary Search Tree (BST).")
else:
    print("The tree is NOT a Binary Search Tree (BST).")


