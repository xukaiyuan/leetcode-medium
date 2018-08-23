class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if(num == 0):
            return [0]
        res = [0, 1]

        i = 2
        k = 2

        while(i <= num):
            for i in range(2 ** (k - 1), 2 ** k):
                if(i > num):
                    break
                halfRangeLength = 2 ** (k - 1) - 2 ** (k - 2)
                if(i < 2 ** (k - 1) + halfRangeLength):
                    res.append(res[i - halfRangeLength])
                else:
                    res.append(res[i - halfRangeLength] + 1)
            k += 1
        return res
