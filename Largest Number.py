import functools
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            if(x + y >= y + x):
                return 1
            else:
                return -1

        result = "".join(sorted(map(str, nums), key=functools.cmp_to_key(compare), reverse = True))
        if(result[0] == "0"):
            return "0"
        else:
            return result
        
        