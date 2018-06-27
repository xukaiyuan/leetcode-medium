class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find(nums, target, start, end):
            if(start > end):
                return -1
            mid = int((end + start) / 2)
            if(nums[mid] == target):
                return mid
            if(nums[mid] < nums[end]):
                if(nums[mid] < target and target <= nums[end]):
                    return find(nums, target, mid + 1, end)
                else:
                    return find(nums, target, start, mid - 1)
            else:
                if(nums[mid] > target and target >= nums[start]):
                    return find(nums, target, start, mid - 1)
                else:
                    return find(nums, target, mid + 1, end)

        length = len(nums)
        return find(nums, target, 0, length - 1)

