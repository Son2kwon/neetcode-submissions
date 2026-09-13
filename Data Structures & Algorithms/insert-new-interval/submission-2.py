class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals += [newInterval]
        intervals.sort()
        
        ans = [intervals[0]]; n = len(intervals)

        for i in range(1, n):
            cur = ans.pop(-1)
            nxt = intervals[i]
            tmp = []
            cstart = cur[0]; cend = cur[1]; nstart = nxt[0]; nend = nxt[1];

            if cstart <= nstart and nstart <= cend:
                tmp = [min(cstart, nstart), max(cend, nend)]
                ans.append(tmp)
            else:
                ans.append(cur)
                ans.append(nxt)


        return ans
            

# Intervals는 처음 들어보는 거네.
# 겹치는 부분들 해서 가장 길게 이으라는 거네.

# 가장 쉬운 풀이는 start를 기준으로 sorting 한 다음에
# 끝날 때마다 ans에 append하는 느낌이 가장 쉬울 것 같은데..

# 