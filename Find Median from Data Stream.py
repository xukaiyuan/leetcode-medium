from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.minHeap, num)
        heappush(self.maxHeap, -heappop(self.minHeap))

        if(len(self.maxHeap) > len(self.minHeap)):
            heappush(self.minHeap, -heappop(self.maxHeap))


    def findMedian(self):
        """
        :rtype: float
        """
        if(len(self.minHeap) > len(self.maxHeap)):
            return float(self.minHeap[0])
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()