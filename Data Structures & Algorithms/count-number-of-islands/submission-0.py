class Solution:
    visited: List[List[bool]]

    def __init__(self):
        visited = []

    def findCandidates(self, row: int, col: int, row_max: int, col_max: int):
        delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        candidates = []

        for di, dj in delta:
            nr = row + di; nc = col + dj;

            if 0 <= nr < row_max and 0 <= nc < col_max:
                candidates.append([nr, nc])

        return candidates

    def DFS(self, grid: List[List[str]], row: int, col: int):
        if grid[row][col] == "0"  or self.visited[row][col]:
            return

        candidates = self.findCandidates(row, col, len(grid), len(grid[0]))

        self.visited[row][col] = True
        
        for i, j in candidates:
            self.DFS(grid, i, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid); col = len(grid[0])

        self.visited = [[False for _ in range(0, col)] for _ in range(0, row)]

        ans = 0

        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == "1" and not self.visited[i][j]:
                    ans += 1
                    self.DFS(grid, i, j)

        return ans

        
# 그래프로 바꾼 다음에 visited 쓰면 될 것 같은데?
# 굳이 그래프로 바꿀 것도 없지, 그냥 [str, bool] 을 한 칸으로 하는 2차원 배열 만들면 똑같은데?
# 아니지, visited라는 2차원 배열 하나만 써도 되지.
# 근데 DFS를 써야 하니까 함수를 만들긴 해야겠다.