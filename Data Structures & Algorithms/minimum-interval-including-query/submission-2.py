class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []; d = dict()

        intervals = sorted(intervals); sortedQueries = sorted(queries)
        heap = []; i = 0

        for q in sortedQueries:
            if q in d:
                continue

            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while len(heap) > 0 and heap[0][1] < q:
                heapq.heappop(heap)

            if len(heap) == 0:
                d[q] = -1
            else:
                d[q] = heap[0][0]

        for q in queries:
            ans.append(d[q])

        return ans

# 각 쿼리의 숫자가 속하는 intervals 중에 가장 짧은 interval의 길이를 구하라는 건데
# Brute Force로 풀면 m*n 정도의 시간으로 풀 수 있을테지만
# 역시나 TLE가 뜨네.

# 오프라인 쿼리, 쿼리 자체를 정렬해서 유리한 순서로 처리한다라...
# 쿼리가 오름차순으로 정렬되어 있다면 좀 편하긴 하겠다.

# 힌트1: Brute Force는 O(m*n)이다. 더 좋은 방법은 없을까? 쿼리를 정렬한다면 더 좋을텐데.
# 뭐야 결국 알고 있던 내용이었네.
# 쿼리를 오름차순으로 정렬한다면... intervals를 모두 돌 필요는 없겠지

# 힌트2: intervals를 start를 기준으로 정렬, 쿼리도 정렬. interval들을 min-heap에 넣는다.
# interval[0] <= q 이면 q의 output 후보 -> min-heap에 넣는다 (기준은 size)
# 다음 q가 min-heap의 [0]에 포함된다면, 그대로 출력하면 끝
# 아 근데 ans의 q 자리가 고정되어 있네.

# 힌트3: min-heap은 size를 기준으로 heappush. min-heap[0]의 end가 q보다 작다면 pop
# start 기준으로 intervals를 sorting, queires sorting
# intervals[i][0] <= q 이면 heappush
# heap[0][1] < q 이면 heappop
# ans.append(heap[0][0])

# 이제 size는 다 나온 것 같은데, 순서를 어떻게 맞추냐는건데...
# 억지로 맞추려면 hashmap 쓰면 되긴 해

# 이젠 답이 아예 틀리네
# query에 같은 값이 들어올 수 있으니까, 그것까지 생각을 해야하는데
# 차라리 query에 대한 답을 hash에 저장해두고, 그걸 query를 돌면서 해결할까?