class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxIndex = 0

        if(len(nums) == 0):
            return False
        for i in range(len(nums)):
            if(i > maxIndex):
                break
            maxIndex = max(maxIndex, i + nums[i])
        return maxIndex >= len(nums) - 1