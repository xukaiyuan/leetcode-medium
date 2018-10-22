class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if(len(s) < len(t)):
            return 0
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range((m + 1))]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(m):
            for j in range(n):
                if(s[i] == t[j]):
                    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]

        return dp[m][n]