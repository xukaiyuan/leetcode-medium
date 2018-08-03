class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        while(n != 0):
        	if(self.isUgly(res)):
        		n -= 1
        	else:
        		res += 1
        return res
        
    def isUgly(self, i):
    	if(i == 1):
    		return True
    	while(i % 2 == 0):
    		i /= 2
    	while(i % 3 == 0):
    		i /= 3
    	while(i % 5 == 0):
    		i /= 5
    	return (i == 1)


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        
        i2 = 0
        i3 = 0
        i5 = 0
        
        while(len(res) < n):
            m2 = res[i2] * 2
            m3 = res[i3] * 3
            m5 = res[i5] * 5
            
            min_m = min(m2, m3, m5)
            res.append(min_m)
            if(min_m == m2):
                i2 += 1
            if(min_m == m3):
                i3 += 1
            if(min_m == m5):
                i5 += 1
            
        return res[-1]