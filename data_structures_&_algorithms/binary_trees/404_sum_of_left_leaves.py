"""
https://leetcode.com/problems/sum-of-left-leaves/description
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0

    res = 0
    q = deque()
    left_nodes = []
    q.append(root)

    while q:
        curr = q.popleft()
        if curr.left:
            q.append(curr.left)
            left_nodes.append(curr.left)

        if curr.right:
            q.append(curr.right)

        # Check if curr node is leaf node
        if not curr.left and not curr.right:
            # Check if this leaf node is in left_nodes
            if curr in left_nodes:
                res += curr.key

    return res        