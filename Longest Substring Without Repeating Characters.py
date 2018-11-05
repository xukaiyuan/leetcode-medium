class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = set()
        i = 0
        j = 0
        res = 0

        while(i < len(s) and j < len(s)):
            if(s[j] in record):
                record.remove(s[i])
                i += 1
            else:
                record.add(s[j])
                j += 1

            res = max(res, j - i)

        return res