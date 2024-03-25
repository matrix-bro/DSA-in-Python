"""
https://leetcode.com/problems/search-in-a-binary-search-tree/description/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root is None: return

    if val == root.val:
        return root
    elif val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)