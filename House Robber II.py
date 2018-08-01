class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        elif(len(nums) == 1):
            return nums[0]
        elif(len(nums) == 2):
            return max(nums[0], nums[1])

        dp1 = self.dp(nums[0:-1])
        dp2 = self.dp(nums[1:])

        return max(dp1[-1], dp2[-1])

    def dp(self, nums):
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp