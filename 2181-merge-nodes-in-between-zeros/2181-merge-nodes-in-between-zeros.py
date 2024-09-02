# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr_new = dummy
        curr = head.next
        summ = 0
        while curr:
            if curr.val!=0:
                summ += curr.val
            else:
                if summ != 0:
                    curr_new.next = ListNode(summ)
                    curr_new = curr_new.next
                    summ = 0
            curr = curr.next
        return dummy.next
                