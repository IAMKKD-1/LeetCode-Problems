# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        nex = None
        while curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        start = head
        while prev.next:
            t1 = start.next
            t2 = prev.next
            start.next, prev.next = prev, start.next
            start = t1
            prev = t2
        
