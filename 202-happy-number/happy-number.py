class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        check = set()

        
        while n not in check:
            
            check.add(n)
            sumofSquare = 0

            while n > 0:

                digit = n%10
                sumofSquare += digit**2
                n = n//10
        
            if sumofSquare == 1:
                return True
            
            n = sumofSquare
        return False