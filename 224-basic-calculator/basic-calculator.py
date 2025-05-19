class Solution:
    def calculate(self, s: str) -> int:
        
        j = 0
        sign = 1
        res = 0
        num = 0
        stack = []

        while (j < len(s)):
            
            i = s[j]
            if (i.isdigit()):
                num = num*10 + int(i)
            elif (i == "+"):
                res += sign*num
                sign = 1
                num = 0
            elif (i == "-"):
                res += sign*num
                sign = -1
                num = 0
            elif (i == "("):
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif (i ==")"):
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
            
            j += 1
        
        res += sign*num
        return res
