class Solution:
    d: dict
    visited: set
    def __init__(self):
        self.d = dict()
        self.visited = set()

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        for ui, vi, ti in times:
            if ui not in self.d:
                self.d[ui] = []

            self.d[ui].append([vi, ti])

        heap = []; heapq.heappush(heap, [0, k]); ans = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in self.visited:
                continue
            ans = time

            self.visited.add(node)

            for nxt_node, cost in self.d.get(node, []):
                heapq.heappush(heap, [time + cost, nxt_node])

        for i in range(1, n+1):
            if i not in self.visited: return -1

        return ans
        

# 결국 Graph로 돌아왔구만.

# directed, weighted graph인데, k부터 시작해서 모든 node가 다 받을 때까지 걸리는 최소 시간

# BFS로 하면 될 것 같은데?
# 시뮬레이션을 돌린다고 하면, 현재 time보다 queue에 있는 time이 적으면 다시 queue에 넣는 식으로
# 그래서 마지막에 time을 return 하면...

# cur_time을 쓰는 정확하지 않아
# 차라리 BFS로 마지막 노드에 걸리는 최솟값을 업데이트 하는게..

# 힌트1: 모든 노드로 도착하는 shortest path를 찾는 알고리즘. heap-based 알고리즘이 도움이 될 지도?
#   진짜 다익스트라인가?