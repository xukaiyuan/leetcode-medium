class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if(len(s) < len(p)):
            return []
        dict1 = [0] * 26
        dict2 = [0] * 26
        res = []
        
        for i in range(len(p)):
            dict1[ord(p[i]) - ord('a')] += 1
            dict2[ord(s[i]) - ord('a')] += 1
        if(dict1 == dict2):
            res.append(0)
        
        for i in range(1, len(s) - len(p) + 1):
            dict2[ord(s[i - 1]) - ord('a')] -= 1
            dict2[ord(s[i + len(p) - 1]) - ord('a')] += 1
            if(dict1 == dict2):
                res.append(i)
        return res
            