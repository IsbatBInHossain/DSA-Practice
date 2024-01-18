import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        r1 = head
        r2 = head.next
        while r2:
            new = ListNode(math.gcd(r1.val, r2.val))
            new.next = r2
            r1.next = new
            r1 = r2
            r2 = r2.next
        return head

        