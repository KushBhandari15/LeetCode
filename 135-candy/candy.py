class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        size = len(ratings)
        candies = [1] * len(ratings)

        for i in range(1, size):
            if (ratings[i] > ratings[i-1]):
                candies[i] = candies[i-1] + 1

        for j in range(size-2, -1, -1):
            if (ratings[j] > ratings[j+1]):
                if (candies[j] <= candies[j+1]):
                    candies[j] = candies[j+1] + 1


        return sum(candies)