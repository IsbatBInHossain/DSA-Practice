from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Without using extra stack
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        firstHalf = prev
        secondHalf = slow
        maxPair = 0

        while firstHalf and secondHalf:
            maxPair = max(maxPair, firstHalf.val + secondHalf.val)
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        
        return maxPair
