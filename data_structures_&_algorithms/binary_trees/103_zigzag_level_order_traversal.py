"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    
    res = []
    queue = deque()
    queue.append(root)
    z = 0
    
    while queue:
        curr_list = []
        for _ in range(len(queue)):
            curr = queue.popleft()
            curr_list.append(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        if z % 2 == 0:
            res.append(curr_list)
        else:
            res.append(curr_list[::-1])
        z += 1
    return res