class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        dic = {}
        res = []
        if(len(s) < 10):
        	return res
        for i in range(len(s) - 9):
        	tmp = s[i:i + 10]
        	if(tmp in dic):
        		dic[tmp] += 1
        	else:
        		dic[tmp] = 1
        	if(dic[tmp] == 2):
        		res.append(tmp)
        return res