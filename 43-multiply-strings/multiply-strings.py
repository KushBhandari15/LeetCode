class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        helperMap = {"0": 0, "1" : 1, "2": 2, "3": 3,
                    "4" : 4, "5": 5, "6": 6,
                    "7": 7, "8": 8, "9": 9}

        number1 = 0
        for i in range (len(num1)):
            number1 = (10*number1) + helperMap[num1[i]]

        number2 = 0
        for i in range (len(num2)):
            number2 = (10*number2) + helperMap[num2[i]]

        res = number1 * number2

        if res == 0:
            return "0"
        
        # Convert result back to string manually
        result_str = ""
        while res > 0:
            result_str = chr(res % 10 + ord('0')) + result_str
            res = res // 10
        
        return result_str

