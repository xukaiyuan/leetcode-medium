class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Floyd's Tortoise and Hare (Cycle Detection)
        slow = nums[0]
        fast = nums[0]

        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow == fast):
                break

        slow = nums[0]

        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow