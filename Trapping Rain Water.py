class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if(len(height) == 0):
            return 0

        rightPeak = [None] * len(height)
        leftPeak = [None] * len(height)
        
        leftPeak[0] = 0
        rightPeak[-1] = 0
        
        for i in range(1, len(height)):
            leftPeak[i] = max(leftPeak[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            rightPeak[i] = max(rightPeak[i + 1], height[i + 1])

        res = 0
        for i in range(len(height)):
                cur = min(rightPeak[i], leftPeak[i]) - height[i]
                if(cur > 0):
                    res += cur

        return res