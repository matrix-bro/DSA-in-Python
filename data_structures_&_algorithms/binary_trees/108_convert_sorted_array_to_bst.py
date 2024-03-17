"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if len(nums) == 0:
        return 
    
    mid = (0 + len(nums) - 1) // 2
    left = nums[:mid]
    right = nums[mid+1:]

    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(left)
    node.right = sortedArrayToBST(right)

    return node

tree = sortedArrayToBST([-10,-3,0,5,9])
tree2 = sortedArrayToBST([1,3])