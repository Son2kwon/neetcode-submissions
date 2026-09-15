class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals); n = len(intervals); 
        prevEnd = intervals[0][1]; count = 0
        
        for i in range(1, n):
            if prevEnd > intervals[i][0]:
                prevEnd = min(prevEnd, intervals[i][1])
                count += 1
            else:
                prevEnd = intervals[i][1]

        return count

# 아주 별 걸 다 하네..
# 전부 overlapping이 안 되기 위해 몇 개를 없애야 하는가? 에 대한 물음인데

# sorting 한 다음에 하나씩 훑으면서 바로 직전과 overlapping되는 게 있으면
# 가능한 앞에, 가능한 짧게 하는 애들만 남긴다.

# 힌트1: interval이 sorted 되어 있다면, first_interval[1] > second_interval[0] 면 overlapped
# 힌트2: Brute Force는 exponential, Greedy가 도움이 될 지도?
# 종합하자면 sorting 한 다음에 overlapped 확인, 앞에 있는 걸 남기고 뒤에 걸 없앤다 (end_time이 더 뒤일 테니까)

# two pointers 사용해서 그 사이 overlapped 부분 전부 count += 1 하면서 센다면...

# 힌트3: sort하고, prevEnd를 저장하면서 track
# prevEnd보다 작은 start를 가진 애들을 전부 세면서 가다가, prevEnd보다 큰 start를 만나면 그 interval의 end값을 prevEnd로 update
# 그래 two pointer를 안 써도 되는 건 알겠는데, 계속 edge case가 나오네..

# 힌트4: overlap 안 되면 prevEnd update. overlap된다면, prevEnd = min(prevEnd, intervals[i][1])
# 이해는 하겠는데, prevEnd의 업데이트가...