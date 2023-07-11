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
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        # print(f"Data: {data}")

        node = TreeNode(data[1])
        # print(f"Node: {node.key}")

        node.left = parse_tuple(data[0])
        # print(f"Node left: {node.left.key if node.left else None}")

        node.right = parse_tuple(data[2])
        # print(f"Node Right: {node.right.key if node.right else None}")

    elif data is None:
        node = None
    else:
        print(f"Single data: {data}")
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
    print(f"Key: {node.key if node else None}")

    if isinstance(node, TreeNode):
        print(f"Node Key: {node.key}")
        if node.left is None and node.right is None:
            return node.key
    
        # print((tree_to_tuple(node.left), node.key, tree_to_tuple(node.right)))
        return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))

print('-----------------')
print(f"Tree to Node: {tree_to_tuple(tree)}")