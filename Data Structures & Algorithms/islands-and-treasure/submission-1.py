class Solution:
    def findCandidates(self, row: int, col: int, max_row: int, max_col: int, visited: List[List[bool]]) -> List[List[int]]:
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        candidates = []

        for di, dj in delta:
            ni = row + di; nj = col + dj;
            if 0 <= ni < max_row and 0 <= nj < max_col and not visited[ni][nj]:
                candidates.append([ni, nj])

        return candidates

    def BFS(self, grid: List[List[int]], row: int, col: int, visited: List[List[bool]]):
        import queue

        queue = queue.Queue()
        max_row = len(grid); max_col = len(grid[0])

        candidates = self.findCandidates(row, col , max_row, max_col, visited)

        for i, j in candidates:
            queue.put([i, j, 1])

        while queue.qsize() > 0:
            i, j, depth = queue.get()

            if grid[i][j] == -1:
                continue

            visited[i][j] = True

            if depth < grid[i][j]:
                grid[i][j] = depth

            candidates = self.findCandidates(i, j, max_row, max_col, visited)

            for ni, nj in candidates:
                queue.put([ni, nj, depth + 1])

        

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        max_row = len(grid); max_col = len(grid[0]);

        for i in range(0, max_row):
            for j in range(0, max_col):
                if grid[i][j] == 0:
                    visited = [[False for _ in range(0, max_col)] for _ in range(0, max_row)]
                    visited[i][j] = True
                    self.BFS(grid, i, j, visited)

# 생각보다 단순하게 풀면 될 것 같은데..
# DFS로 판단하다보면 될 것 같긴 한데

# i, j 에서 출발했다는 걸 표시할 무언가가 필요해
# 아.. 이건 일종의 백트래킹을 사용해야 하는 문제구나? True로 바꿨다가 False로 다시 돌려야 하는...

# DFS로 푸나 했더니, 이거 BFS로 풀어야 하나..?