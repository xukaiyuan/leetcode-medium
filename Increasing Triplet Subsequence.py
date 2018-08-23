import sys
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp1 = sys.maxsize
        tmp2 = sys.maxsize

        for i in nums:
        	if(tmp1 >= i):
        		tmp1 = i
        	elif(tmp2 >= i):
        		tmp2 = i
        	else:
        		return True
        return False
        
