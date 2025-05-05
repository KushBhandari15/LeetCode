class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romanSymbols = {"I": 1, "V": 5, "X": 10, "L" : 50,
                        "C" : 100, "D": 500, "M": 1000}
        
        size = len(s)
        res = 0
        for i in range (size):
            j = i + 1
            curr = romanSymbols[s[i]]

            if (j < size):
                if (romanSymbols[s[i]] < romanSymbols[s[j]]) :
                    res -= romanSymbols[s[i]]
                else:
                    res += romanSymbols[s[i]]
            else:
                res += romanSymbols[s[i]]

        return res
        