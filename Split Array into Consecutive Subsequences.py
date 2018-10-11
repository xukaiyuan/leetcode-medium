class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newdict = {nums[0]:[1]}
        for num in nums[1:]:
            if num not in newdict: newdict[num] = []
            if num-1 in newdict:
                newdict[num] = [newdict[num-1][-1] + 1] + newdict[num]
                del newdict[num-1][-1]
                if not len(newdict[num-1]): del newdict[num-1]
            else: newdict[num].append(1)
                
        minlen = min([min(newdict[i]) for i in newdict])
        if minlen < 3: return False
        else: return True