class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prevEnd = float('-inf')
        n = len(intervals)
        count = 0

        for i in range(n):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                count += 1

        return count