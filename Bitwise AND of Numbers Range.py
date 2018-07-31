import sys
class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        max_int = sys.maxsize
        # result should be the same part of all the intergers in binary format from the very left
        while((m & max_int) != (n & max_int)):
            max_int <<= 1
        return max_int & m