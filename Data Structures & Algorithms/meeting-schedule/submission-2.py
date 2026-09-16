"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n == 0: return True
        intervals = sorted(intervals, key=lambda x: x.end)
        prevEnd = intervals[0].end; 

        for i in range(1,  n):
            if intervals[i].start < prevEnd: return False
            prevEnd = intervals[i].end

        return True

# 음... start나 이런 것들이 ascending이라는 조건이 없으니까
# sorting하고
# 앞에서부터 2개씩 보면서 overlapping인지 보면 되지 않을까?

# 생각해보니 class면 sorting이 쉽지 않을 수 있겠네.. start 기준으로 다시 sorting을 할까?

# 그냥 냅다 풀려고 했더니 겹치는 애들이 있네

# Start 기준 말고 end 기준으로 잡는게 제일 좋겠는데?