# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxx = []
        temp = head

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        slow = prev

        while slow:
            maxx.append(temp.val + slow.val)
            slow = slow.next
            temp = temp.next
        print(maxx)
        return max(maxx)