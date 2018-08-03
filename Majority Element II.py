class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Moore Voting

        if(len(nums) == 0):
            return []
        candidate1 = 0
        count1 = 0
        candidate2 = 1
        count2 = 0

        for i in nums:
            if(i == candidate1):
                count1 += 1
            elif(i == candidate2):
                count2 += 1
            elif(count1 == 0):
                count1 = 1
                candidate1 = i
            elif(count2 == 0):
                count2 = 1
                candidate2 = i
            else:
                count1 -= 1
                count2 -= 1

        n = len(nums)
        res = []
        
        for i in [candidate1, candidate2]:
            if(nums.count(i) > n / 3):
                res.append(i)
        return res
