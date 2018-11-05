class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if(len(s) == 0):
            return []

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dictionary = set(wordDict)

        for i in range(len(s)):
            for j in range(i + 1):
                if(dp[j] and s[j: i + 1] in dictionary):
                    dp[i + 1] = 1
                    break

        res = []
        tmp = []
        
        def dfs(s, dictionary, dp, index, tmp, res):
            if(index == len(s)):
                sentence = ""
                for word in tmp:
                    sentence += word
                    sentence += " "
                res.append(sentence[0:-1])
                return
            if(not dp[index]):
                return
            
            for i in range(index, len(s)):
                substring = s[index:i + 1]
                if(substring not in dictionary):
                    continue
                dfs(s, dictionary, dp, i + 1, tmp + [substring], res)
                

        dfs(s, dictionary, dp, 0, tmp, res)
        return res