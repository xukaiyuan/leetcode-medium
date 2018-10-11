import functools 
import queue

def meetingRooms(time):
	def compare(t1, t2):
		return t1[0] - t2[0]

	cmp = functools.cmp_to_key(compare)
	time.sort(key = cmp)
	
	length = len(time)

	prior = queue.PriorityQueue()

		
	for i in range(length):
		if(prior.qsize() != 0):
			if(time[i][0] >= prior.queue[0]):
				prior.get()
		prior.put(time[i][1])
	
	return prior.qsize()


time = [[0, 30], [5, 11], [6, 22]]
res = meetingRooms(time)
print(res)