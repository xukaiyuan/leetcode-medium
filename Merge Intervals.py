# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from functools import cmp_to_key

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if(len(intervals) == 0):
            return []
        def compare(a, b):
            return a.start - b.start

        intervals.sort(key = cmp_to_key(compare))
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if(merged[-1].end >= intervals[i].start):
                merged[-1].end = max(intervals[i].end, merged[-1].end)
            else:
                merged.append(intervals[i])

        return merged
