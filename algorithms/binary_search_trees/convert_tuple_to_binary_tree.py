"""
Convert a tuple with the structure ( left_subtree, key, right_subtree) (where left_subtree and right_subtree are themselves tuples) into binary tree.

Steps:

- We are using a tuple of size 3 as an input.
- We are using recursion to create left and right subtrees for the node
"""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])

    elif data is None:
        node = None
    else:
        node = TreeNode(data)

    return node

tree_tuple = ((1,3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = parse_tuple(tree_tuple)

# Test

print(tree.key)
print(tree.left.key, tree.right.key)
print(tree.left.left.key, tree.left.right, tree.right.left.key, tree.right.right.key)
print(tree.right.left.right.key, tree.right.right.left.key, tree.right.right.right.key)


"""
Tree to Tuple

"""

def tree_to_tuple(node):

    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key
    
        return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))

print('-----------------')
print(f"Tree to Node: {tree_to_tuple(tree)}")