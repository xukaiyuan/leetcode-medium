class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        count = {}
        appeared = {}

        for i in nums:
            if(i in appeared):
                continue
            if(i not in count):
                count[i] = 1
            else:
                del count[i]
                appeared[i] = 1

        for i in count:
            res.append(i)
        return res