# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        queue = [root]

        while queue:
            level = len(queue)
            elems = []

            for i in range (level):
                curr = queue.pop(0)
                elems.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            result.append(elems)
        
        return result[::-1]