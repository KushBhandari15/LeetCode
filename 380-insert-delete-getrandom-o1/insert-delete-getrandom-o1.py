from collections import defaultdict
class RandomizedSet(object):

    def __init__(self):
        self.myDict = {}
        self.size = 0
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.myDict:
            return False

        self.myDict[val] = True
        self.size += 1
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if (val not in self.myDict):
            return False
        
        self.size -= 1
        del self.myDict[val]
        
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """

        if self.size <= 0:
            return None
        randomInt = random.randint(0, self.size-1)
        key = list(self.myDict.keys())[randomInt]

        return key
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()