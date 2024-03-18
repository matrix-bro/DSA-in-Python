"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    result = []        
    stack = []

    while True:
        if root:
            stack.append(root)
            result.append(root.val)
            root = root.left
        else:
            if not stack:
                break

            root = stack.pop()
            root = root.right
    
    return result