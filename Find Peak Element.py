class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []

        end = len(nums) - 1
        if(end == 0):
            return 0
        def bst(nums, start, end, res):
            if(start > end):
                return

            mid = math.floor((end - start) / 2 + start)
            
            if(mid == 0):
                if(nums[mid] > nums[mid + 1]):
                    res.append(mid)
                else:
                    res.append(mid + 1)
            elif(mid == len(nums) - 1):
                if(nums[mid] > nums[mid - 1]):
                    res.append(mid)
            else:
                if(nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]):
                    res.append(mid)
                    
                else:
                    bst(nums, mid + 1, end, res)
                    bst(nums, start, mid - 1, res)

        bst(nums, 0, end, res)
        
        return res[0]


