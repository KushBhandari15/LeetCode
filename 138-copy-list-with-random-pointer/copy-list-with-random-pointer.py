"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        res = ListNode()
        curr, resNode = head, res

        while curr != None:

            temp = Node(curr.val)
            resNode.next = temp
            resNode = resNode.next
            curr = curr.next
        
        resNode.next = None

        curr = head
        resNode = res.next
        while (curr != None):
            random = curr.random 
            temp = res.next

            if random == None:
                resNode.random = None
            else:
                original = head
                while original is not random:
                    temp = temp.next
                    original = original.next

                resNode.random = temp

            curr = curr.next
            resNode = resNode.next
        return res.next
