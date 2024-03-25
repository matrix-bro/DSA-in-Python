"""
https://leetcode.com/problems/validate-binary-search-tree/description/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def inorder(root, curr):
        if root is None: return True

        if not inorder(root.left, curr):
            return False
        
        if not root.val > curr[0]:
            return False

        curr[0] = root.val
        
        return inorder(root.right, curr)

    return inorder(root, [float("-inf")])