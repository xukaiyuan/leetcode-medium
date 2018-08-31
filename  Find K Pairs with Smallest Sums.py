class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        size = min(k, len(nums1) * len(nums2))
        index = [0] * len(nums1)
        res = []

        for i in range(size):
            cur = 0
            sum = nums1[-1] + nums2[-1] + 1
            for j in range(len(nums1)):
                if(index[j] < len(nums2) and sum >= nums1[j] + nums2[index[j]]):
                    cur = j
                    sum = nums1[j] + nums2[index[j]]
            res.append([nums1[cur], nums2[index[cur]]])
            index[cur] += 1

        return res

