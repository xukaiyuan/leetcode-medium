class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        dp = [[0] * length for _ in range(length)]

        for i in range(length - 1, -1, -1):
        	for j in range(i + 1, length):
        		dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][length - 1] >= 0