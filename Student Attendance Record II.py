class Solution:
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0):
            return 1
        if(n == 1):
            return 3
        if(n == 2):
            return 8
        m = 1000000007
        
        A = [0] * n
        P = [0] * n
        L = [0] * n

        A[0] = 1
        P[0] = 1
        L[0] = 1

        A[1] = 2
        A[2] = 4
        L[1] = 3

        for i in range(1, n):
            P[i] = ((A[i - 1] + P[i - 1]) % m + L[i - 1]) % m
            if(i > 1):
                L[i] = ((A[i - 1] + P[i - 1]) % m + (A[i - 2] + P[i - 2]) % m) % m
            if(i > 2):
                A[i] = ((A[i - 1] + A[i - 2]) % m + A[i - 3]) % m       

        return ((A[n - 1] % m + P[n - 1] % m) % m + L[n - 1] % m) % m