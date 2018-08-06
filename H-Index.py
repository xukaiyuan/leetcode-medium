class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        citations.sort()
        
        res = 0
        
        for i in range(length - 1, -1, -1):
            if(citations[i] and citations[i] >= res):
                res = min(citations[i], res + 1)
            else:
                break
        return res
