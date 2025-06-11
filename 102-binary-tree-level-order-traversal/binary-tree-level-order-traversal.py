# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        if not root:
            return result
        
        queue = deque([root])

        while queue:
            
            levelSize = len(queue)
            currResult = []

            for i in range (levelSize):
                currElement = queue.popleft()
                currResult.append(currElement.val)
                
                if currElement.left:
                    queue.append(currElement.left)
                if currElement.right:
                    queue.append(currElement.right)
            
            result.append(currResult)
        
        return result