# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        helper = {}

        res = ListNode()
        resNode = res

        curr = head

        while (curr != None):
            
            helper[curr.val] = helper.get(curr.val, 0) + 1
            curr = curr.next
        
        
        curr = head
        
        while (curr != None):
            
            if helper[curr.val] == 1:
                resNode.next = ListNode(curr.val)
                resNode = resNode.next
            
            curr = curr.next
        
        return res.next
