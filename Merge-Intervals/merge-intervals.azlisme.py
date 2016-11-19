# -*- encoding: utf-8 -*-

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[{}, {}]'.format(self.start, self.end)

    def __repr__(self):
        return self.__str__()

class Solution(object):
    def merge(self, intervals):
        """
        非常直白的算法，也不必多解释了
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(cmp=lambda x, y: cmp(x.start, y.start))
        def merge_into(in_list, inter):
            if not in_list:
                return [inter]
            last = in_list[-1]
            if last.end >= inter.end:
                return in_list
            elif last.end >= inter.start:
                last.end = inter.end
            else:
                in_list.append(inter)
            return in_list
        return reduce(merge_into, intervals, [])


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18)
    ]))
                
