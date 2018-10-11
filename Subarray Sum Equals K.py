class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        record = []
        res = 0
        tmp = 0
        for i in nums:
            tmp += i
            record.append(tmp)

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if(record[j] - record[i] + nums[i] == k):
                    res += 1

        return res


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        record ={0: 1}
        sum = 0
        res = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            if(sum - k in record):
                res += record[sum - k]
            record[sum] = record.get(sum, 0) + 1
            
        return res