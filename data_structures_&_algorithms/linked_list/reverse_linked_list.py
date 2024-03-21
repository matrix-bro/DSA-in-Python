"""
https://leetcode.com/problems/reverse-linked-list/description/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev