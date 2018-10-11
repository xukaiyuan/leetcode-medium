class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
        	return 1
        start = 0
        end = 1
        res = 1
        tmp = 1

        while(end < len(nums)):
        	if(nums[end] > nums[end - 1]):
        		end += 1
        		tmp += 1
        	else:
        		start = end
        		end += 1
        		res = max(res, tmp)
        		tmp = 1
        res = max(res, tmp)
        return res