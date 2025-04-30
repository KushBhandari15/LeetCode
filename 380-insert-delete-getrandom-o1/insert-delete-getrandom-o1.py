class RandomizedSet(object):

    def __init__(self):
        self.myMap = {}
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.myMap:
            return False
        else:
            self.list.append(val)
            self.myMap[val] = len(self.list) - 1
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.myMap:
            return False
        
        index = self.myMap[val]
        lastElement = self.list[-1]
        self.list[index] = lastElement
        self.myMap[lastElement] = index

        self.list.pop()
        del self.myMap[val]
        return True        

    def getRandom(self):
        """
        :rtype: int
        """
        randomNumber = random.randint(0, len(self.list)-1)
        key = self.list[randomNumber]
        return key
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()