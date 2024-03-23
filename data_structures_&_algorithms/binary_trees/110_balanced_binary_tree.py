"""
https://leetcode.com/problems/balanced-binary-tree/description/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:
    def dfs(root):
        if root is None:
            return True, 0
        
        balanced_l, height_l = dfs(root.left)
        balanced_r, height_r = dfs(root.right)

        balanced = balanced_l and balanced_r and abs(height_r - height_l) <= 1
        height = 1 + max(height_l, height_r)
        return balanced, height
    
    return dfs(root)[0]