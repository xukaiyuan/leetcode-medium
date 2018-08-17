class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if(length == 0):
            return 0
        buy = [0] * length
        sell = [0] * length
        cool = [0] * length
        buy[0] = - prices[0]
        for i in range(1, length):
            buy[i] = max(cool[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            cool[i] = max(cool[i - 1], sell[i - 1])
        return sell[-1]