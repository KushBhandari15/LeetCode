# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        result = []
        queue = [root]
        switch = False
        while queue:
            level = len(queue)
            levelElements = []
            for i in range (level):
                curr = queue.pop(0)
                levelElements.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if switch:
                levelElements = levelElements[::-1]
            switch = not switch
            result.append(levelElements)
        
        return result