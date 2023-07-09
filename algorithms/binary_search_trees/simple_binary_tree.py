"""
A simple binary tree
"""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node0 = TreeNode(3)      
node1 = TreeNode(4)      
node2 = TreeNode(5)

# Connect the nodes

node0.left = node1
node0.right = node2

root = node0
print(root)
print(root.key)
print(root.left.key)
print(root.right.key)