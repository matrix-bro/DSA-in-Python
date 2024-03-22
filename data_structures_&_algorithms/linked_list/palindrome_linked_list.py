"""
https://leetcode.com/problems/palindrome-linked-list/description/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    str1 = "" 
    while head:
        str1 += str(head.val)
        head = head.next

    rev_str1 = str1[::-1]
    return True if str1 == rev_str1 else False