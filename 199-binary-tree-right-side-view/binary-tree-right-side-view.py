# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            size = len(queue)
            val = 0
            for i in range(size):
                curr = queue.popleft()
                val = curr.val

                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            
            res.append(val)
        
        return res

