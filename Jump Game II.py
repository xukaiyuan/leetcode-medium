class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        last = 0
        res = 0

        for i in range(len(nums)):
            if(i > last):
                last = cur
                res += 1
            cur = max(cur, nums[i] + i)

        return res