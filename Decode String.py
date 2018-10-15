class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s) == 0):
            return ""

        num = []
        pre = []
        res = ""
        count = 0
        for i in s:
            if(ord(i) - ord("0") > -1 and ord(i) - ord("0") < 10):
                count = count * 10 + int(i)
            elif(i == "["):
                num.append(count)
                pre.append(res)
                res = ""
                count = 0
            elif(i == "]"):
                number = num.pop(-1)
                tmp = ""
                for j in range(number):
                    tmp += res
                res = tmp
                previous = pre.pop(-1)
                res = previous + res
            else:
                res += i

        return res