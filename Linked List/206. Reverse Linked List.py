from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        prev = head
        while prev:
            temp = prev.next
            prev.next = reversed
            reversed = prev
            prev = temp
        return reversed