class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i in self.overlap:
        	if(i[0] < end and i[1] > start):
        		return False

        for i in self.calendar:
        	if(i[0] < end and i[1] > start):
        		self.overlap.append([max(start, i[0]), min(end, i[1])])
        self.calendar.append([start, end])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)