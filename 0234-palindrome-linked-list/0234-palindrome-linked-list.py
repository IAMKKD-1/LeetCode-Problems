# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        stack = []
        while slow:
            stack.append(slow.val)
            slow = slow.next
        curr = head
        while curr and curr.val == stack.pop():
            curr = curr.next
        return curr is None