class Solution:
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        # number of str already contains A
        countA = 1
        # number of str contains 2 continuous L at last
        countL = 0

        if(n == 0):
            return 0
        dp = [0] * (n + 1)
        dp[1] = 3

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * 3 - countA - countL
            countA = countA * 2 + dp[i - 1] - countA
            countL += 1
        return dp[-1]