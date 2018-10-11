import functools 


def meetingRooms(time):
	def compare(t1, t2):
		return t1[0] - t2[0]

	cmp = functools.cmp_to_key(compare)
	time.sort(key = cmp)
	end = time[0][1]
	length = len(time)
	for i in range(length):
		if(time[i][0] < end):
			return False
		end = max(end, time[i][1])
	return True


time = [[0, 30], [5, 11], [6, 22]]
res = meetingRooms(time)
print(res)