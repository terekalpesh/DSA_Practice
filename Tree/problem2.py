# Find the height of a binary tree.

class Node:
    def __init__(self, value):
        self.value = value  # The value of the node
        self.left = None    # Left child
        self.right = None   # Right child


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)  # Create the root node

    def insert_left(self, parent, value):
        """ Insert a node to the left of the given parent node """
        parent.left = Node(value)

    def insert_right(self, parent, value):
        """ Insert a node to the right of the given parent node """
        parent.right = Node(value)

    def height(self, node):
        """ Function to calculate the height of the tree """
        if node is None:
            return -1  # If the node is None, the height is -1 (empty tree)
        else:
            left_height = self.height(node.left)  # Height of the left subtree
            right_height = self.height(node.right)  # Height of the right subtree
            return 1 + max(left_height, right_height)  # Height is 1 + max of left and right heights

tree = BinaryTree(1)  # Root node with value 1

# Inserting nodes
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)

tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

tree.insert_left(tree.root.right, 6)
tree.insert_right(tree.root.right, 7)

# Find the height of the tree
print("Height of the tree:", tree.height(tree.root))  # Output: 2
