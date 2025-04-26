class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = prices[0]
        price = 0

        for i in range (1, len(prices)):
            
            if (min_price > prices[i]):
                min_price = prices[i]

            price = max(price, prices[i] - min_price)


        return price