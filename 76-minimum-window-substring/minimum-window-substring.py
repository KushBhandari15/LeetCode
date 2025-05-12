class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not s or not t:
            return ""

        t_map = {}
        for i in range (len(t)):
            t_map[t[i]] = t_map.get(t[i] , 0) + 1
        

        start = 0
        window = float('inf')
        res = ""
        s_map = {}
        have, need = 0, (len(t_map))

        for end in range (len(s)):
            
            s_map[s[end]] = s_map.get(s[end] , 0) + 1

            if (s[end] in t_map and t_map[s[end]] == s_map[s[end]]):
                have += 1

            while (have == need):

                if (window > (end-start+1)):
                    res = s[start: end+1]
                    window = (end-start+1)
                
                
                s_map[s[start]] -= 1

                if (s[start] in t_map and t_map[s[start]] > s_map[s[start]]):
                    have -= 1

                start += 1


        return res
                

        