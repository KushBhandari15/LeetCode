class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        def pop(stack):
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            
            return num1, num2
        for action in tokens:
            if (action == "+"):
                num1, num2 = pop(stack)
                print(num2, action , num1)
                stack.append(num2 + num1)
            elif (action == "-"):
                num1, num2 = pop(stack)
                print(num2, action , num1)
                stack.append(int(num2 - num1))
            elif (action == "*"):
                num1, num2 = pop(stack)
                print(num1, action , num2)
                stack.append(num2*num1)
            elif (action == "/"):
                num1, num2 = pop(stack)
                print(num2, action , num1)
                print(int(num2/num1))
                stack.append(int(num2/num1))
            else:
                stack.append(action)

        return int(stack[0])