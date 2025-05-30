# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if (k==0):
            return head
        helper = []
        curr = head
        while (curr != None):
            helper.append(curr)
            curr = curr.next

        size = len(helper)    
        res = ListNode()
        resNode = res
        for i in range (size):

            newIndex = (i-k + size) % size
            node = helper[newIndex]
            node.next = None
            resNode.next = node
            resNode = resNode.next
        
        return res.next