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
        
        if not head:
            return None

        res = {}

        curr = head
        while (curr):
            res[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                res[curr].next = res[curr.next]
            if curr.random:
                res[curr].random = res[curr.random]
            
            curr = curr.next
        
        return res[head]