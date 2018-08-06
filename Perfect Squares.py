import sys
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if(n < 0):
            return 0
        dp = [sys.maxsize] * (n + 1)

        for i in range(int(math.sqrt(n)) + 1):
            dp[i * i] = 1
        for a in range(n):
            for b in range(int(math.sqrt(n - a)) + 1):
                dp[a + b * b] = min(dp[a] + 1, dp[a + b * b])
        return dp[n]