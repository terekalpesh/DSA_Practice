# Implement pre-order, in-order, and post-order traversal of a binary tree.

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

    def in_order_traversal(self, node):
        """ In-order traversal (Left, Root, Right) """
        if node:
            self.in_order_traversal(node.left)
            print(node.value, end=" ")
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        """ Pre-order traversal (Root, Left, Right) """
        if node:
            print(node.value, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        """ Post-order traversal (Left, Right, Root) """
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=" ")



tree = BinaryTree(1)  # Root node with value 1

# Inserting nodes
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)

tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

tree.insert_left(tree.root.right, 6)
tree.insert_right(tree.root.right, 7)

print("In-order traversal:")
tree.in_order_traversal(tree.root)  # Output: 4 2 5 1 6 3 7

print()
print("Pre-order traversal:")
tree.pre_order_traversal(tree.root)  # Output: 1 2 4 5 3 6 7

print()
print("Post-order traversal:")
tree.post_order_traversal(tree.root)  # Output: 4 5 2 6 7 3 1

print()