class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        record = set()
        res = 1

        for i in nums:
            record.add(i)

        for i in nums:
            curLen = 0
            current = i
            if(len(record) == 0):
                break
            while(current in record):
                record.remove(current)
                curLen += 1
                current += 1

            current = i - 1
            while(current in record):
                record.remove(current)
                curLen += 1
                current -= 1

            res = max(res, curLen)

        return res