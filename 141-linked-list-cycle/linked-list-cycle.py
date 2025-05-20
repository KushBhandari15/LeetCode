# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if (head == None):
            return False
        curr = head
        fast = head

        while fast and fast.next:

            curr = curr.next
            fast = fast.next
            fast = fast.next

            if (curr == fast):
                return True
        
        return False

        