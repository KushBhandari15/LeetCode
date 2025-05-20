# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        res = ListNode()
        resNode = res

        curr1, curr2 = list1, list2
        
        while (curr1 != None or curr2 != None):
            
            val1 = 101
            val2 = 101
            if (curr1):
                val1 = curr1.val
            if (curr2):
                val2 = curr2.val

            if (val1 < val2):
                resNode.next = ListNode(val1)
                resNode = resNode.next
                curr1 = curr1.next
            else:
                resNode.next = ListNode(val2)
                resNode = resNode.next
                curr2 = curr2.next
        

        return res.next