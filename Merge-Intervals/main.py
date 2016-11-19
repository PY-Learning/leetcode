#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        res = []
        current = intervals[0]
        for i in intervals[1:]:
            if current.end >= i.start and i.end >= current.end:
                current.end = i.end
            else:
                res.append(current)
                current = i
        else:
            if len(res) == 0: res = [intervals[0]]

        if intervals[-1].start > res[-1].end:
            res.append(current)
        return res


if __name__ == "__main__":
    test_data = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    test_data = [Interval(1,4), Interval(0,5)]
    test_data = [Interval(1,4), Interval(1,5)]
    for i in Solution().merge(test_data):
        print (i.start, i.end)
