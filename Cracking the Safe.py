class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = "0" * (n - 1)
        visited = set()
        
        for i in range(k ** n):
            if(n > 1):
                lastN = res[1-n:]
            else:
                lastN = ""
            
            for j in range(k - 1, -1, -1):
                if(lastN + str(j) not in visited):
                    visited.add(lastN + str(j))
                    res += str(j)
                    break
                    
        return res