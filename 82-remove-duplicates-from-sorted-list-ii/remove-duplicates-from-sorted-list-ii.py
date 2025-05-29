# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        resNode = res

        curr = head
        prev = -101
        count = 0
        while (curr != None):

            if (prev != curr.val or prev == -101):
                if (count == 1):
                    resNode.next = ListNode(prev)
                    resNode = resNode.next
                prev = curr.val
                count = 1
            else:
                count += 1
            
            curr = curr.next
        
        if (count == 1):
            resNode.next = ListNode(prev)
            resNode = resNode.next
        
        return res.next

