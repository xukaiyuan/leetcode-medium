class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        base = 1
        res = []
        for i in range(len(nums)):
            res.append(base)
            base *= nums[i]
        base = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= base
            base *= nums[i]
        return res