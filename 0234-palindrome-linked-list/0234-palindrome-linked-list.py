# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # slow = head
        # stack = []
        # while slow:
        #     stack.append(slow.val)
        #     slow = slow.next
        # curr = head
        # while curr and curr.val == stack.pop():
        #     curr = curr.next
        # return curr is None

        def reverse(head):
            prev = None
            curr = head
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            return prev

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
