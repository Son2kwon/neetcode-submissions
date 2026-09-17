"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals); 
        if n == 0: return 0
        start = []; end = []; ans = float('-inf')

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort(); end.sort()

        s = 0; e = 0; count = 0

        while s < n:
            while s < n and start[s] < end[e]:
                s += 1; count += 1

            ans = max(ans, count)
            e += 1
            count -= 1

        return ans


# 겹칠 때마다 room 하나씩 추가하면 되지 않나? 가 아니구나
# prevEnd로 훑다가 겹치는 게 있다면 그 때마다 count += 1하면 되는 거 아닌가?

# 겹칠 때마다 count += 1을 하면, 다른 방에 넣을 수 있는데 못 넣는 그런 상황이 발생하는구나
# 각 방마다 end 값만 저장해둔다면...

# 그치 이러면 시간은 많이 쓸테니까 TLE...

# 힌트1: 필요한 방의 수는 maximum number of overlapping meetings at any point on the number line.
# 힌트2: 2개의 배열을 생성한 다음에 start와 end를 각각 저장. 두 배열을 sorting 한 다음에 two-pointer 접근.
# 어... 어떤 의미인지는 대충 감이 잡히는데, 정확하게는 모르겠네. 두 배열을 각각 sorting하면 의미가 날라가는데

# start <= end 일 때까지 start += 1, room +=1 이런 느낌으로 하면 될 것 같은데
# sorting 기준을 뭘로 해야하지? start 기준으로 하면 안 되는데, end 기준으로 하면 되는 것은 같은데

# 힌트3: start[s] <= end[e] 가 True 인 지점 안에서 s 증가, count 증가
# end를 기준으로 sorting, start와 end 배열 사용
# while start[s] < end[e]: 
#   s += 1; count += 1;
# ans = max(ans, count); count = 0; e = s;

# 아 이것도 뭔가 아닌데...

# 힌트4: 그리고, e = s로 update. ans = max(ans, count)
# 아니 뭐 내가 생각한 거랑 똑같네...