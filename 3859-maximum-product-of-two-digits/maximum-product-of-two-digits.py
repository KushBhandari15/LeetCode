class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        arr = []
        
        while (n > 0):
            
            current = n%10
            arr.append(current)
            n = n//10
        
        res = 0
        
        arr.sort()
        size = len(arr)
        if (len(arr) > 1):
            return arr[size-1] * arr[size-2]
        else:
            return arr[0]
        
        