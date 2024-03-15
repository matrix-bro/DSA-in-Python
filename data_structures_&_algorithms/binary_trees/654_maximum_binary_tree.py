"""
https://leetcode.com/problems/maximum-binary-tree/description/

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
    if len(nums) == 0:
        return
    
    max_idx = nums.index(max(nums))    
    left_prefix = nums[:max_idx]
    right_suffix = nums[max_idx+1:]

    node = TreeNode(nums[max_idx])
    node.left = constructMaximumBinaryTree(left_prefix)
    node.right = constructMaximumBinaryTree(right_suffix)

    return node

print(constructMaximumBinaryTree([3,2,1,6,0,5]))
print(constructMaximumBinaryTree([3,2,1]))