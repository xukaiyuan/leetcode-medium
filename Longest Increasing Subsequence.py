class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if(length == 0):
            return 0

        dp = [0] * length
        dp[0] = 1

        for i in range(1, length):
            tmp = []
            for j in range(0, i):
                if(nums[i] > nums[j]):
                    tmp.append(dp[j])
            if(tmp != []):
                dp[i] = max(tmp) + 1
            else:
                dp[i] = 1
        return max(dp)