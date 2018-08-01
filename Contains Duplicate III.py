class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if(t == 0 and len(nums) == len(set(nums))):
            return False
        for i in range(0, len(nums)):
            for j in range(i + 1, i + k + 1):
                if(j >= len(nums)):
                    break           
                if(abs(nums[j] - nums[i]) <= t):
                    return True
        return False
