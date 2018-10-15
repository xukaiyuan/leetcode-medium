class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return nums[0]
        start = 0
        end = len(nums) - 1
        if(nums[start] < nums[end]):
            return nums[0]
        while(start < end):
        	mid = int((end - start) / 2 + start)
        	if(nums[mid] > nums[mid + 1]):
        		return nums[mid + 1]
        	if(nums[mid - 1] > nums[mid]):
        		return nums[mid]

        	if(nums[mid] > nums[0]):
        		start = mid + 1
        	else:
        		end = mid
        