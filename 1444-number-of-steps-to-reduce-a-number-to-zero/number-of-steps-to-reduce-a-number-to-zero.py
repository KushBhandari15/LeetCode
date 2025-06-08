class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        def helper (num, steps = 0):

            if num == 0:
                return steps

            if (num%2==0):
                return helper(num/2, steps+1)
            else:
                return helper(num-1, steps+1)
        
        return helper(num)
