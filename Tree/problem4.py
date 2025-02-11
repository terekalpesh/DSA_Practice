# Find the lowest common ancestor (LCA) of two nodes in a binary tree.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if root is None or root == p or root == q:
        return root
    
    # Look for LCA in left and right subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # If both nodes are found in left and right, root is the LCA
    if left and right:
        return root
    
    # If one of the nodes is found, return that node
    return left if left else right

# Creating the tree nodes
root = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)

# Connecting nodes
root.left = node5
root.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4

# Finding LCA of node5 and node1
LCA = lowest_common_ancestor(root, node5, node1)
print(LCA.value)
