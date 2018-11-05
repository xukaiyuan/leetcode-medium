class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []

        def backTracking(n, remain, res, tmp, start):
        	if(remain < 0):
        		return 

        	if(remain == 0):
        		res.append(tmp)

        	for i in range(start, n + 1):
        		backTracking(n, remain - 1, res, tmp + [i], i + 1)

        backTracking(n, k, res, tmp, 1)
        return res