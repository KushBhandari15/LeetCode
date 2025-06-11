# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []
        
        result = []
        queue = []
        queue.append(root)

        while queue:
            levelSize = len(queue)
            cumulative = 0

            for i in range (levelSize):
                currElement = queue.pop(0)
                cumulative += currElement.val
                if currElement.left:
                    queue.append(currElement.left)
                if currElement.right:
                    queue.append(currElement.right)
            
            average = cumulative/levelSize
            result.append(average)
        
        return result