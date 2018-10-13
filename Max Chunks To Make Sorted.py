class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maximum = -1
        res = 0

        for i in range(len(arr)):
            maximum = max(maximum, arr[i])
            if(i == maximum):
                res += 1

        return res 