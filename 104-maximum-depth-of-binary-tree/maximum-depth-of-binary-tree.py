# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.height = 0

    def getHeight(self, node):

        if node == None:
            return 0
        
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        curr = max(leftHeight, rightHeight) + 1
        self.height = max(self.height, curr)

        return curr
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.getHeight(root)
        return self.height
        

