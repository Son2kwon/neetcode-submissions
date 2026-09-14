class Solution:
    def isOverlapped(self, a_start: int, a_end: int, b_start: int, b_end: int):
        return not (a_end < b_start or b_end < a_start)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []; n = len(intervals); intervals = sorted(intervals)
        ans.append(intervals[0]); i = 1

        while i < n:
            if self.isOverlapped(ans[-1][0], ans[-1][1], intervals[i][0], intervals[i][1]):
                cur = ans.pop(-1)
                ans.append([min(cur[0], intervals[i][0]), max(cur[1], intervals[i][1])])
            else:
                ans.append(intervals[i])

            i += 1
        
        return ans

# 오케이, 일단 merge 자체는 어렵지 않은데, 이제 어디까지 영향을 미칠거냐는 새로 봐야한다는거잖아.
# 저번에는 그래도 순서대로 줬는데, 이번엔 아니니까..
# 그러면 sorting 하고 똑같이 하면 되잖아?

# interval을 매번 받아온 다음에, 
#   overlapped 된다면 cur을 merge
#   overlapped 안 된다면 cur을 ans에 넣고 빈 칸으로 update

# Time Complexity: O(n log n)
# Space Complexity: O(1)