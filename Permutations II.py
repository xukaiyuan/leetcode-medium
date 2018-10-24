class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backTracking(nums, tmp, res):
            if(not nums):
                res.append(tmp)
                return
            else:
                for i in range(len(nums)):
                    if(i > 0 and nums[i - 1] == nums[i]):
                        continue
                    backTracking(nums[:i] + nums[i + 1:], tmp + [nums[i]], res)

        res = []
        nums.sort()
        backTracking(nums, [], res)
        return res