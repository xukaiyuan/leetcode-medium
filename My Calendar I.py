class MyCalendar:

    def __init__(self):
        self.interval = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i in self.interval:
            if(i[0] < end and i[1] > start):
                return False
        self.interval.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)