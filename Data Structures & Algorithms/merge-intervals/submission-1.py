class Solution:
    def isOverlapped(self, a_start: int, a_end: int, b_start: int, b_end: int):
        return not (a_end < b_start or b_end < a_start)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []; cur = []; n = len(intervals); i = 0;

        intervals = sorted(intervals)

        while i < n:
            interval = intervals[i]

            if cur == []:
                cur = interval
                i += 1
            elif self.isOverlapped(cur[0], cur[1], interval[0], interval[1]):
                cur = [min(cur[0], interval[0]), max(cur[1], interval[1])]
                i += 1
            else:
                ans.append(cur)
                cur = []
        
        if cur != []:
            ans.append(cur)

        return ans

# 오케이, 일단 merge 자체는 어렵지 않은데, 이제 어디까지 영향을 미칠거냐는 새로 봐야한다는거잖아.
# 저번에는 그래도 순서대로 줬는데, 이번엔 아니니까..
# 그러면 sorting 하고 똑같이 하면 되잖아?

# interval을 매번 받아온 다음에, 
#   overlapped 된다면 cur을 merge
#   overlapped 안 된다면 cur을 ans에 넣고 빈 칸으로 update