# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for i in range(left-1):
            prev = prev.next
        
        curr = prev.next
        for i in range(right-left):
            nex = curr.next
            curr.next = nex.next
            nex.next = prev.next
            prev.next = nex
        return dummy.next
                   
        
        
        # def reverse(curr, end):
        #     prev = curr
        #     while curr and curr != end:
        #         nex = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = nex
        # dum = ListNode()
        # dum.next = head
        # dummy = head
        # c = 1
        # while dummy:
        #     if c == left:
        #         curr = dummy.next
        #     if c == right:
        #         last = dummy.next
        #         break
        #     dummy = dummy.next
        #     c += 1
        
        # reverse(curr, last)
        # return dum.next