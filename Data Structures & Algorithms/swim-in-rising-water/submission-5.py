class Solution:
    def inGrid(self, x: int, y: int, n: int):
        return 0 <= x and x < n and 0 <= y and y < n

    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [[grid[0][0], 0, 0]]; n = len(grid);
        visited = [[False for _ in range(n)] for _ in range(n)]

        while heap:
            t, cx, cy = heapq.heappop(heap)
            if visited[cx][cy]: continue
            if cx == n-1 and cy == n-1: return t

            visited[cx][cy] = True

            lx = cx; ly = cy - 1
            rx = cx; ry = cy + 1
            dx = cx + 1; dy = cy
            ux = cx - 1; uy = cy

            if self.inGrid(lx, ly, n) and not visited[lx][ly]:
                cost = 0
                if grid[lx][ly] > t:
                    cost = grid[lx][ly] - t

                heapq.heappush(heap, [t + cost, lx, ly])

            if self.inGrid(rx, ry, n) and not visited[rx][ry]:
                cost = 0
                if grid[rx][ry] > t:
                    cost = grid[rx][ry] - t

                heapq.heappush(heap, [t + cost, rx, ry])
            
            if self.inGrid(dx, dy, n) and not visited[dx][dy]:
                cost = 0
                if grid[dx][dy] > t:
                    cost = grid[dx][dy] - t

                heapq.heappush(heap, [t + cost, dx, dy])

            if self.inGrid(ux, uy, n) and not visited[ux][uy]:
                cost = 0
                if grid[ux][uy] > t:
                    cost = grid[ux][uy] - t

                heapq.heappush(heap, [t + cost, ux, uy])
            


# 문제 이해하는데만 4분 썼네

# t = k일 때
# 이웃 칸의 숫자 <= k라면 cost = 0
# 이웃 칸의 숫자 > k라면 cost = (이웃 칸의 숫자) - (현재 칸의 숫자)
# min_heap 쓰고, 매 순간 가장 작은 cost의 칸을 사용한다면... 그리고 그 cost만큼 t를 업데이트

# 뭐가 계속 안되네...

# 힌트 1: 그래프로 생각. Greedy approach가 도움이 될 지도?
#   그래서 그냥 heap을 사용하려는건데...

# 어우 TLE가 뜨네...

# 힌트 2: maximum elevation이 최소가 되는 path를 찾아야 한다. Shortest Path Algorithm이 도움이 될 듯?
#   그래서 다익스트라 썼는데...

# 힌트 3: 다익스트라 쓰면 돼.
#   맞잖아.. 근데 왜 TLE가 뜨지?

# 사소한 오류들 고쳤는데도 계속 TLE가 뜨는데..

# 아오 진짜 TLE의 지옥...