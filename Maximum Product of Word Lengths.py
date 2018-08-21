class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        if(length == 0 or length == 1):
            return 0
        bits = [0] * length

        for i in range(length):
            for j in words[i]:
                bits[i] |= 1 << (ord(j) - 97)

        res = 0
        for i in range(length):
            for j in range(i + 1, length):
                if(not bits[i] & bits[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res
