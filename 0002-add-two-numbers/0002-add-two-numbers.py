# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        power = 1

        while l1:
            num1 = l1.val * power + num1
            power *= 10
            l1 = l1.next
        power = 1
        while l2:
            num2 = l2.val * power + num2
            power *= 10
            l2 = l2.next
        
        ans = num1 + num2
        dummy = ListNode()
        if ans == 0:
            return dummy
        curr = dummy
        while ans:
            temp = ListNode(val = ans % 10)
            ans = ans // 10
            curr.next = temp
            curr = curr.next
        return dummy.next
