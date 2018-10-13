class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        index = []

        res = [0] * len(T)

        for i in range(len(T)):
            while(len(stack) != 0 and T[i] > stack[-1]):
                stack.pop(-1)
                id = index.pop(-1)
                res[id] = i - id
            stack.append(T[i])
            index.append(i)

        return res
