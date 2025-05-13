class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anaMap = defaultdict(list)

        for word in strs:
            
            key = tuple(sorted(word))

            anaMap[key].append(word)


        return anaMap.values()