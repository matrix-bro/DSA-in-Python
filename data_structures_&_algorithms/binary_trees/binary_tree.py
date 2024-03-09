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

# tree_tuple = ((1,3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree_tuple = ((((1, 2, None), 3, ((None, 4, 5), 6, (7, 8, 9)))))
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
print(f"Tree to Tuple: {tree_to_tuple(tree)}")

"""
Display Tree

Input:
        2
    3                 5
1       ø       3           7
            ø       4   6       8      


Output:
            8
        7
            6
    5
            4
        3  
            ø
2
        ø
    3
        1
"""
def display_tree(node, space='\t', level=0):
    if node == None:
        print(space * level + "ø")
        return

    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return
    
    display_tree(node.right, space, level=level+1)
    print(space * level + str(node.key))
    display_tree(node.left, space, level=level+1)

print('\n--------Displaying Tree---------')
display_tree(tree)

"""
Preorder Traversal
"""
def preorder_traversal(node):
    if node == None:
        return
    print(node.key, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)

print('\n--------Preorder Traversal---------')
preorder_traversal(tree)

"""
Inorder Traversal
"""
def inorder_traversal(node):
    if node == None:
        return
    inorder_traversal(node.left)
    print(node.key, end=" ")
    inorder_traversal(node.right)

print('\n\n--------Inorder Traversal---------')
inorder_traversal(tree)

"""
Postorder Traversal
"""
def postorder_traversal(node):
    if node == None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.key, end=" ")

print('\n\n--------Postorder Traversal---------')
postorder_traversal(tree)

"""
Height of a Binary Tree
"""
def tree_height(node):
    if node is None: return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

print(f'\n\nTree Height: {tree_height(tree)}')

"""
Size of a Tree / Number of nodes in a Binary Tree
"""
def tree_size(node):
    if node is None: return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

print(f'\nTree Size: {tree_size(tree)}')