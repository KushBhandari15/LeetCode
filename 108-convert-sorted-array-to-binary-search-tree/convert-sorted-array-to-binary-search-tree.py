# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):

        self.root = None
    def insert(self, val):

        def helper(node, val):
            if not node:
                return TreeNode(val)
            
            if node.val > val:
                node.left = helper(node.left, val)
            else:
                node.right = helper(node.right, val)
            
            return node
        
        self.root = helper(self.root, val)
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(nums, start, end):

            if start >= end:
                return

            mid = (start+end) // 2
            self.insert(nums[mid])
            helper(nums, start, mid)
            helper(nums, mid+1, end)

        
        helper(nums, 0, len(nums))
        return self.root