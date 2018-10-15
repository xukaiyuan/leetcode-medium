class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        tmp = []

        for i in range(len(arr)):
        	tmp.append(arr[i])
        	copy = tmp[:]
        	if(copy == tmp.sort()):
        		res += 1
        		tmp = []

        return res


