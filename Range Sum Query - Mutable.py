class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.binaryIndexTree = [0] * (len(nums) + 1)
        self.nums = nums
        for i in range(len(nums)):
            self.add(i, nums[i])

    def lowbit(self, k):
        # determine how many elements in nums will be summed in position k
        return k & (-k)

    def add(self, i, val):
        i += 1
        while(i < len(self.binaryIndexTree)):
            self.binaryIndexTree[i] += val
            i += self.lowbit(i) 

    def read(self, i):
        # sum from 1 to i
        sum = 0
        i += 1
        while(i):
            sum += self.binaryIndexTree[i]
            i -= self.lowbit(i)   
        return sum

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        dif = val - self.nums[i]
        self.nums[i] = val
        self.add(i, dif)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.read(j) - self.read(i - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)