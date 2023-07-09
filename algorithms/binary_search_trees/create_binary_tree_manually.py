class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

root = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(6)
node8 = TreeNode(8)

# Connect Nodes

root.left = node1
root.right = node2

root.left.left = node3

root.right.left = node4
root.right.right = node5

root.right.left.right = node6

root.right.right.left = node7
root.right.right.right = node8


print(root.key)
print(root.left.key)
print(root.right.key)

print(root.left.left.key)

print(root.right.left.key)
print(root.right.right.key)

print(root.right.left.right.key)

print(root.right.right.left.key)
print(root.right.right.right.key)



