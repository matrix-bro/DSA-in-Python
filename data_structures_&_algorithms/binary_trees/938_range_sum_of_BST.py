"""
https://leetcode.com/problems/range-sum-of-bst/description/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    def wrapper(node, count):
        if node is None:
            return
        
        if low <= node.val <= high:
            count[0] += node.val
        
        wrapper(node.left, count)
        wrapper(node.right, count)

        return count[0]

    return wrapper(root, [0])