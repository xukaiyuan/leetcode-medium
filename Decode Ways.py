class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = int((s[0] != "0"))

        for i in range(2, len(s) + 1):
            first = int(s[i - 1: i])
            second = int(s[i - 2: i])
            if(first != 0):
                dp[i] = dp[i - 1]
            if(second > 9 and second < 27):
                dp[i] += dp[i - 2]
        return dp[-1]