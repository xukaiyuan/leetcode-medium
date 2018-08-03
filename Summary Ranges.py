class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if(len(nums) == 0):
            return res
        tmp = str(nums[0])
        s = []
        s.append(nums[0])
        end = False
        for i in range(1, len(nums)):
            if(nums[i] != s[-1] + 1):
                if(len(s) != 1):
                    tmp += "->"
                    tmp += str(s[-1])
                res.append(tmp)                      
                tmp = str(nums[i])
                s = []
            elif(i == len(nums) - 1):
                tmp += "->"
                tmp += str(nums[i])
                res.append(tmp)
                s = []
                end = True
            s.append(nums[i])
        if(len(s) != 0 and end == False):
            res.append(str(s[0]))
        return res
