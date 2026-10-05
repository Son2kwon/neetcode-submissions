class Solution:
    def find(self, parent: List[int], x: int):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])

        return parent[x]

    def union(self, parent: List[int], x: int, y: int):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
        

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1: return 0

        edges = []; parent = [i for i in range(n)]

        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                edges.append([cost, i, j])

        heapq.heapify(edges)

        edge_count = 0; ans = 0

        while edge_count < n - 1:
            cost, a, b = heapq.heappop(edges)

            # 사이클이 있으면
            if self.find(parent, a) == self.find(parent, b):
                continue

            # 사이클이 없으면
            self.union(parent, a, b)

            edge_count += 1
            ans += cost

        return ans

        

# 힌트 1: Advanced Graph algorithm that can be used to connect all points into one component?
#   BFS랑 DFS 말하는건가?

# 힌트 2: Kruskal's 알고리즘을 사용하면 된다. Final Component는 MST를 구성한다. 
# Kruskal algorithm: 간선을 기준으로 선택해서, MST를 그릴 수 있는 알고리즘
#   1. 간선들을 가중치에 따라 오름차순으로 정렬
#   2. 가장 작은 간선들 중에서 사이클을 형성하지 않는 간선을 고른다.
#   3. 해당 간선을 MST에 추가한다.
#   4. 선택한 간선의 수가 V - 1이 될 때까지 진행한다.