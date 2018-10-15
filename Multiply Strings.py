class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def reverse(s):
        	r = ""
        	for i in range(len(s) - 1, -1, -1):
        		r += s[i]
        	return r

        num1 = reverse(num1)
        num2 = reverse(num2)

        res = "0" * (len(num1) + len(num2))

        for i in range(len(num2)):
        	tmp = 0
        	multiple = ord(num2[i]) - ord("0")

        	for j in range(len(num1)):
        		tmp += multiple * (ord(num1[j]) - ord("0")) + ord(res[i + j]) - ord("0")
        		res[i + j] = str(tmp % 10)
        		tmp /= 10

        	if(tmp != 0):
        		res[len(num1) + i] == str(tmp)

        res = reverse(res)

        count = 0
        while(count < len(res) and res[count] == "0"):
        	count += 1

        return res[count:]