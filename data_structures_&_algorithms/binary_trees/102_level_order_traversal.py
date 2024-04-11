"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    
    res = []
    queue = deque()
    queue.append(root)

    while queue:
        curr_list = []
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            curr_list.append(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)
        res.append(curr_list)
    
    return res