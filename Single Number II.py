class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = dict()
        for i in range(len(nums)):
            if(nums[i] not in hashmap):
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        for key in hashmap:
            if(hashmap[key] == 1):
                return key