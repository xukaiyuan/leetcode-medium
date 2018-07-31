import sys
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = sys.maxsize
        sum = 0
        start = 0

        for i in range(len(nums)):
            sum += nums[i]
            while(sum >= s):
                res = min(res, i + 1 - start)
                sum -= nums[start]
                start += 1
        if(res == sys.maxsize):
            return 0
        else:
            return res