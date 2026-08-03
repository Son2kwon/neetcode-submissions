class Solution:
    row_max: int
    col_max: int
    visited: List[List[bool]]
    queue: List

    def __init__(self):
        self.row_max = 0
        self.col_max = 0
        self.visited = []
        self.queue = collections.deque()

    def findCandidates(self, board: List[List[str]], row: int, col: int):
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        candidates = []

        for di, dj in delta:
            ni = row + di; nj = col + dj;
            if 0 <= ni < self.row_max and 0 <= nj < self.col_max and \
            not self.visited[ni][nj] and board[ni][nj] == "O":
                self.visited[ni][nj] = True
                candidates.append([ni, nj])

        return candidates

    def traverse(self, board: List[List[str]]):
        while self.queue:
            i, j = self.queue.popleft()

            candidates = self.findCandidates(board, i, j)

            for candidate in candidates:
                self.queue.append(candidate)
                
    def solve(self, board: List[List[str]]) -> None:
        self.row_max = len(board); self.col_max = len(board[0]);
        self.visited = [[False for _ in range(self.col_max)] \
        for _ in range(self.row_max)]

        for i in range(self.row_max):
            if board[i][0] == "O":
                self.visited[i][0] = True
                self.queue.append([i, 0])
            if board[i][self.col_max - 1] == "O":
                self.visited[i][self.col_max - 1] = True
                self.queue.append([i, self.col_max - 1])

        for i in range(self.col_max):
            if board[0][i] == "O":
                self.visited[0][i] = True
                self.queue.append([0, i])
            if board[self.row_max - 1][i] == "O":
                self.visited[self.row_max - 1][i] = True
                self.queue.append([self.row_max - 1, i])

        self.traverse(board)

        for i in range(self.row_max):
            for j in range(self.col_max):
                if not self.visited[i][j]:
                    board[i][j] = "X"

# 바둑인데..?
# 2중 for문 돌다가 O를 만나면 DFS로 탐색하다가, 마지막 부분에 edge에 닿아있으면 True, 안 닿아있으면 False
# False 라면 빠져나오면서 O를 X로 바꿔준다.

# 아, 이것도 가장자리에 있는 O부터 시작해서 BFS로 들어가는게 더 낫겠다..