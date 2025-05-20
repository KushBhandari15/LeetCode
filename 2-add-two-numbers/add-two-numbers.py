# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        resNode = res
        curr1, curr2 = l1, l2
        carry = 0
        while (curr1 or curr2):
            temp = carry
            if (curr1):
                temp += curr1.val
                curr1 = curr1.next
            if (curr2):
                temp += curr2.val
                curr2 = curr2.next

            carry = temp // 10
            resNode.next = ListNode(temp%10)
            resNode = resNode.next
        
        if carry != 0:
            resNode.next = ListNode(carry)
            resNode = resNode.next
        return res.next
            

