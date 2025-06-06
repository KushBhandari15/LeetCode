class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def rec (nums, target, s, e):
            if (s > e):
                return -1
            
            m = s + (e-s) // 2

            if nums[m] == target:
                return m
            
            if (nums[m] > target):
                return rec(nums, target, s, m-1)
            
            return rec(nums, target, m + 1, e)
        
        return rec(nums, target, 0, len(nums) -1)