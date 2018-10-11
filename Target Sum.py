class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        matrix = [[1] * len(nums) for _ in range(2)]
        for i in range(len(nums)):
            matrix[1][i] = -1
        res = [0]
        self.dfs(nums, matrix, S, 0, 0, 0, res)
        self.dfs(nums, matrix, S, 1, 0, 0, res)
        return res[0]

    def dfs(self, nums, matrix, S, i, j, tmp, res):
        if(j == len(nums) - 1):
            if(tmp + matrix[i][j] * nums[j] == S):
                res[0] += 1
                return
            else:
                return
        else:
            self.dfs(nums, matrix, S, 0, j + 1, tmp + matrix[i][j] * nums[j], res)
            self.dfs(nums, matrix, S, 1, j + 1, tmp + matrix[i][j] * nums[j], res)
