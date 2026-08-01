class Solution:
    remain: int
    cur: int

    def __init__(self):
        self.remain = 0
        self.cur = 0
    
    def findCandidates(self, row: int, col: int, max_row: int, max_col: int, visited: List[List[bool]], grid: List[List[int]]) -> List[List[int]]:
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        candidates = []

        for drow, dcol in delta:
            nrow = row + drow; ncol = col + dcol;
            if 0 <= nrow < max_row and 0 <= ncol < max_col and not visited[nrow][ncol]:
                visited[nrow][ncol] = True
                if grid[nrow][ncol] == 0:
                    continue
                candidates.append([nrow, ncol])

        return candidates

    def BFS(self, grid: List[List[int]]):
        max_row = len(grid); max_col = len(grid[0]);
        visited = [[False for _ in range(0, max_col)] for _ in range(0, max_row)]
        queue = collections.deque()

        for i in range(0, max_row):
            for j in range(0, max_col):
                if grid[i][j] == 2:
                    visited[i][j] = True
                    queue.append([i, j, self.cur])

        while queue:
            i, j, depth = queue.popleft()

            if grid[i][j] == 0:
                continue
            
            if grid[i][j] == 1:
                self.remain -= 1

            candidates = self.findCandidates(i, j, max_row, max_col, visited, grid)

            for row, col in candidates:
                queue.append([row, col, depth + 1])
                self.cur = max(self.cur, depth + 1)



    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_row = len(grid); max_col = len(grid[0]);
        for i in range(0, max_row):
            for j in range(0, max_col):
                if grid[i][j] == 1:
                    self.remain += 1

        self.BFS(grid)

        if self.remain > 0:
            return -1
        else:
            return self.cur
        

# BFS로 가장 큰 depth를 가지는 숫자를 찾으면...
# 대신 BFS로 접근하지 못하는 1인 칸이 있으면 -1

# 2가 여러개 있을 수 있으니까 얘도 multi-source BFS를 사용해야겠다.
# rotten 배열, visited boolean 배열, remain_fresh 변수