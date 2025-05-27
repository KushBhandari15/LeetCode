# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        res = ListNode()
        resNode = res

        helper = []
        curr = head
        while (curr != None):
            helper.append(curr)
            curr = curr.next
        
        index = 0
        while (index + k <= len(helper)):
            upper = index + k
            lower = index
            for i in range (upper-1, lower-1, -1):
                resNode.next = helper[i]
                resNode = resNode.next
            index = upper
        
        while index < len(helper):
            resNode.next = helper[index]
            resNode = resNode.next
            index += 1
        
        resNode.next = None
        return res.next
