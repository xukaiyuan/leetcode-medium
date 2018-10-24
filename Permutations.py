class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums) < 1):
            return [[]]
        def backTracking(nums, tmp, res):
            if(len(tmp) == len(nums)):
                res.append(tmp)
                return
            else:
                for num in nums:
                    if(num not in tmp):
                        backTracking(nums, tmp + [num], res)

        res = []

        backTracking(nums, [], res)
        return res