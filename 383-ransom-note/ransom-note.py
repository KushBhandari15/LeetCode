class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """


        helper = {}
        for letter in magazine:

            helper[letter] = helper.get(letter, 0) + 1
        

        for letter in ransomNote:

            occ = helper.get(letter, 0)

            if (occ > 0):
                helper[letter] -= 1
            
            else:
                return False
        
        return True
        