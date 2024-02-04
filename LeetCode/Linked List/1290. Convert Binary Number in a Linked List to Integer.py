# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decNum = 0
        current = head
        i = -1
        while current:
            i += 1
            current = current.next
        while head:
            decNum += 2**i*head.val
            head = head.next
            i-=1
        return decNum