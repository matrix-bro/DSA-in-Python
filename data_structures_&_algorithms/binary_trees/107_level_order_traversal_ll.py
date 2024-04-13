"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    res = deque()
    queue = deque()
    queue.append(root)

    while queue:
        curr_list = []
        for _ in range(len(queue)):
            curr = queue.popleft()
            curr_list.append(curr.val)

            if curr.left:
                queue.append(curr.left)      
            if curr.right:
                queue.append(curr.right)  
        res.appendleft(curr_list)
    
    return res