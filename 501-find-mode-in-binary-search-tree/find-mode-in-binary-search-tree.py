# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        count = {}
        if not root:
            return []
        def helper(node):
            nonlocal count

            if not node:
                return
            
            count[node.val] = count.get(node.val, 0) + 1

            helper(node.left)
            helper(node.right)

        helper(root)
        max_freq = max(count.values())
        return [k for k, v in count.items() if v == max_freq]