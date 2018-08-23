class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """     
        nums.sort()
        tmp_nums = nums[:]
        length = len(nums)
        n = len(nums)
        k = int((length + 1) / 2)
        for i in range(length):
            if(i % 2 == 0):
                nums[i] = tmp_nums[k - 1] 
                k -= 1
            else:
                nums[i] = tmp_nums[n - 1]
                n -= 1