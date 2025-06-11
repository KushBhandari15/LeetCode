"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None

        result = []
        queue = deque([root])

        while queue:
            level = len(queue)
            prev = None

            for i in range (level):
                curr = queue.popleft()

                if prev:
                    prev.next = curr
                prev = curr

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            prev.next = None
        
        return root
