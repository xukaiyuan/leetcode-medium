class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix)
        if(row == 0):
        	return False
        column = len(matrix[0])

        start_row = 0
        start_column = 0
        end_row = row - 1
        end_column = column - 1

        while(start_row < end_row):
        	mid_row = int((start_row + end_row) / 2)
        	if(matrix[mid_row][-1] == target):
        		return True
        	elif(matrix[mid_row][-1] < target):
        		start_row = mid_row + 1
        	else:
        		end_row = mid_row
        if(start_row > end_row):
        	return False
       	while(start_column < end_column):
       		mid_column = int((start_column + end_column) / 2)
       		if(matrix[start_row][mid_column] == target):
       			return True
       		elif(matrix[start_row][mid_column] < target):
       			start_column = mid_column + 1
       		else:
       			end_column = mid_column - 1
       	if(start_column > end_column):
       		return False
       	else:
       		return (matrix[start_row][start_column] == target)

