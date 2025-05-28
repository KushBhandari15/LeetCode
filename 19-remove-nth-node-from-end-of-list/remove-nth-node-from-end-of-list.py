# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        size = 0
        while (curr != None):
            curr = curr.next
            size += 1
        
        if n == size:
            return head.next
        curr = head
        for i in range (0, (size-n-1)):
            curr = curr.next
        
        curr.next = curr.next.next if curr.next else None

        return head