class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ''
        if(numRows >= len(s) or numRows == 1):
            return s

        else:
            for i in range(numRows):
                tmp = i
                if(tmp % numRows == 0 or tmp % numRows == numRows - 1):
                    while(tmp < len(s)):
                        result += s[tmp]
                        tmp += 2 * (numRows - 1)
                else:
                    result += s[i]
                    tmp1 = tmp + 2 * (numRows - i % numRows - 1)
                    tmp2 = tmp + 2 * (numRows - 1)
                    while(tmp2 < len(s)):
                        if(tmp1 != i):       
                            result += s[tmp1] 
                        result += s[tmp2]
                        tmp1 += 2 * (numRows - 1)
                        tmp2 += 2 * (numRows - 1)
                    if(tmp1 < len(s)):
                        result += s[tmp1]
        return result