class Solution:
    ans: int
    visited: List[List[bool]]

    def __init__(self):
        self.ans = 0

    def findCandidates(self, i: int, j: int, max_row: int, max_col: int) -> List[List[int]]:
        delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        candidates = []

        for di, dj in delta:
            ni = i + di; nj = j + dj;
            if 0 <= ni < max_row and 0 <= nj < max_col:
                candidates.append([ni, nj])

        return candidates

    def DFS(self, grid: List[List[int]], row: int, col: int) -> int:
        if grid[row][col] == 0 or self.visited[row][col]:
            return 0

        self.visited[row][col] = True
            
        max_row = len(grid); max_col = len(grid[0]);

        candidates = self.findCandidates(row, col, max_row, max_col)

        cur = 0
        
        for i, j in candidates:
            cur += self.DFS(grid, i, j)

        return cur + 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid); col = len(grid[0]);
        self.visited = [[False for _ in range(0, col)] for _ in range(0, row)]

        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 1 and not self.visited[i][j]:
                    cur = self.DFS(grid, i, j)

                    if self.ans < cur:
                        self.ans = cur

        return self.ans
        
# 저번 거랑 똑같이 하는데, 이번엔 area를 찾으면서 접근한다.