class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = []
        length = len(nums)
        res = [-1] * length
        
        for i in range(length * 2):
            num = nums[i % length]
            while(len(st) != 0 and nums[st[-1]] < num):
                res[st[-1]] = num
                st.pop(-1)
            if(i < length):
                st.append(i)
        
        
        return res
                