class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res = [False] * (len(s) + 1)
        res[0] = True
        for i in range(len(s)):
            for j in range(0, i + 1):
                tmp = s[j:i + 1]
                if(res[j] and tmp in wordDict):
                    res[i + 1] = True
                    break 

        return res[-1]