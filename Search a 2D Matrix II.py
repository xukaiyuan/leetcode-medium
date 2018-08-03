class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix) == 0):
            return False
        width = len(matrix[0])

        for i in matrix:
            if(self.bs(i, 0, width - 1, target)):
                return True
        return False

    def bs(self, array, start, end, target):
        while(start <= end):
            mid  = int((start + end) / 2)   		
            if(array[mid] < target):
                start = mid + 1
            elif(array[mid] == target):
                return True
            else:
                end = mid - 1
        return False
