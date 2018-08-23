class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        tmp = [[] for _ in range(len(nums) + 1)]
        for key in count:
            tmp[count[key]].append(key)

        res = []
        for i in range(len(tmp) - 1, -1, -1):
            if(len(tmp[i]) == 0):
                continue
            for j in tmp[i]:
                res.append(j)
                if(len(res) == k):
                    return res
