# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        res = ListNode()
        resNode = res

        ref = []
        curr = head
        while (curr != None):
            temp = ListNode(curr.val)
            ref.append(temp)
            curr = curr.next

        for i in range (0, left-1):
            resNode.next = ref[i]
            resNode = resNode.next

        for i in range (right-1, left-2, -1):
            resNode.next = ref[i]
            resNode = resNode.next
        
        for i in range (right, len(ref)):
            resNode.next = ref[i]
            resNode = resNode.next
        
        resNode.next = None
        return res.next
        

          

        