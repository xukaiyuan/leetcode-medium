class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
        	return x + y > y + x

        strs = map(str, nums)
        print(strs)