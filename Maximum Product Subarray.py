class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return nums[0]
        length = len(nums)
        max_product = [0] * length
        min_product = [0] * length
        max_product[0] = nums[0]
        min_product[0] = nums[0]

        for i in range(1, length):
            max_product[i] = max(max(nums[i] * max_product[i - 1], nums[i] * min_product[i - 1]), nums[i])
            min_product[i] = min(min(nums[i] * max_product[i - 1], nums[i] * min_product[i - 1]), nums[i])

        return max(max_product)