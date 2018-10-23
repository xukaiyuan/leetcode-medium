class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = "*#"
        for i in range(len(s)):
            new += s[i] + "#"

        radius = [0] * len(new)
        id = 0
        mx = 0
        maxLen = 0
        pos = 0

        for i in range(1, len(new)):
            if(i > mx):
                radius[i] = 1
            else:
                radius[i] = min(radius[2 * id - i], mx - i)

            while(i + radius[i] < len(new) and new[i - radius[i]] == new[i + radius[i]]):
                radius[i] += 1

            if(radius[i] + i > mx):
                mx = radius[i] + i
                id = i
            
            if(radius[i] > maxLen):
                maxLen = radius[i]
                pos = i
            
        start = int((pos - maxLen) / 2)
        return s[start: start + maxLen - 1]