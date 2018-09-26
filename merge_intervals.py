# 56. Merge Intervals
"""
Given a collection of intervals, merge all overlapping intervals.
Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""

# Definition for an interval.
class Interval:
    def __ini__(self, s=0, e=0):
    self.start = s
    self.end = e

def merge(self, intervals):
    res = []
    for i in sorted(intervals, key= lambda i: i.start):
        if res and i.start <= res[-1].end :  # i.start <= res[-1].end  :  case of overlap
            out[-1].end = max(out[-1].end, i.end)  # pick up max end value
        else:
            out += i  # add the case which has no overlap
    return res

# Time O(n) # Space O(1)

