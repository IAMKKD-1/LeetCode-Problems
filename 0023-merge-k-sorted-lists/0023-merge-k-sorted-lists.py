# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        t = []
        for i in lists:
            while i:
                t.append(i.val)
                i = i.next
        
        t.sort()
        for i in t:
            new = ListNode(i)
            dummy.next = new
            dummy = dummy.next
        return head.next