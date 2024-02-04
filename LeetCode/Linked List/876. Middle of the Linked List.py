# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Uses the runner method 
        r1 = head
        r2 = head
        while r2 and r2.next:
                r1 = r1.next
                r2 = r2.next.next
        return r1
        
        