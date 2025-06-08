class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True
        
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s)
        def palindrome(s, start, end):
            
            if (start >= end):
                return True

            if (s[start] != s[end]):
                return False
            
            return palindrome(s, start+1, end-1)

        return palindrome(s, 0, len(s)-1)
        

        

            
            
        