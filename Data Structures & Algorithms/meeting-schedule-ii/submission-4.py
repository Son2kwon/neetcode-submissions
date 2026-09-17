"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0: return 0

        intervals = sorted(intervals, key=lambda x: x.start)
        end = [];

        count = 0; ans = 0; 

        for interval in intervals:
            if len(end) == 0:
                heapq.heappush(end, interval.end)
                count += 1

            else:
                heapq.heappush(end, interval.end)
                count += 1
            
            while len(end) > 0 and interval.start >= end[0]:
                heapq.heappop(end)
                count -= 1

            ans = max(ans, count)

        return ans

# [시작, 끝] 쌍을 굳이 가지고 있을 필요가 없는 이유는, 그냥 그 순간에 회의 하나 시작하면 room += 1, 끝나면 room -= 1하면 되니까. 어떤 회의가 진행되고 있는지는 중요하지 않아.
# start를 기준으로 정렬된 intervals를 가져와서
# heap의 최솟값 > start 라면 room += 1
# heap의 최솟값 <= start 라면 heap의 최솟값 > start 일때까지 heappop(), count -= 1

# Time Complexity:
# Space Complexity: 