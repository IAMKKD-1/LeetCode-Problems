# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next = head)
        if not head or not head.next:
            return None
        len = 0
        checker = head
        while checker:
            len += 1
            checker = checker.next
        len = len - n
        new = dummy
        for i in range(len):
            new = new.next
        new.next = new.next.next
        return dummy.next