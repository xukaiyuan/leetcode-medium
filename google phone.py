def convert(index, numOfCol):
	if(index == 0):
		return [3, 1]
	else:
		index -= 1
		row = int(index / numOfCol)
		col = index - numOfCol * row
	return [row, col]

def helper(row, result, numOfOperation):
	step = abs(numOfOperation)
	if(row):
		operation = "up" if(numOfOperation > 0) else "down"
		for j in range(step):
			result.append(operation)
	else:
		operation = "left" if(numOfOperation > 0) else "right"
		for j in range(step):
			result.append(operation)

def sequence(nums, numOfCol):
	if(len(nums) == 0):
		return []
	result = ["enter"]
	for i in range(len(nums) - 1):
		first = convert(nums[i], numOfCol)
		second = convert(nums[i + 1], numOfCol)

		rowOperation = first[0] - second[0]
		colOperation = first[1] - second[1]

		helper(0, result, colOperation)
		helper(1, result, rowOperation)
		result.append("enter")

	return result


nums = [6, 4, 8, 9]
result = sequence(nums, 6)
print(result)