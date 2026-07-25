class Solution:
    ans: List[List[str]]
    used: List[List[bool]]
    stack: List[List[int]]
    count: List[int]

    def __init__(self):
        self.used = []
        self.ans = []
        self.stack = []
        self.count = []

    def updateBaord(self, n: int, row: int, col: int):
        cur = 0
        for i in range(0, n):
            if self.used[row][i]:
                self.used[row][i] = False
                self.stack.append([row, i])
                cur += 1

            if self.used[i][col]:    
                self.used[i][col] = False
                self.stack.append([i, col])
                cur += 1

        for i in range(0, n):
            for j in range(0, n):
                if (i + j) == (row + col) and self.used[i][j]:
                    self.used[i][j] = False
                    self.stack.append([i, j])
                    cur += 1
                if (i - j) == (row - col) and self.used[i][j]:
                    self.used[i][j] = False
                    self.stack.append([i, j])
                    cur += 1

        self.count.append(cur)

    def undoBoard(self, row: int):
        n = self.count.pop()
        for i in range(0, n):
            r, c = self.stack.pop()
            self.used[r][c] = True


    def backTrack(self, n: int, depth: int, cur: List[str]):
        if n == depth:
            self.ans.append(cur.copy())
            return

        status = ["." for _ in range(n)]
        for i in range(0, n):
            if self.used[depth][i]:
                status[i] = "Q"; cur.append("".join(status))
                self.updateBaord(n, depth, i)
                self.backTrack(n, depth + 1, cur)

                status[i] = "."; cur.pop()
                self.undoBoard(depth)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.used = [[True for _ in range(n)] for _ in range(n)]

        self.backTrack(n, 0, [])

        return self.ans

# 결국 N-Queen 문제까지 왔구나...

# if n == depth:
#   ans 업데이트, return

# for i in range(0, n):
#   수평, 수직, 대각선을 확인
#       된다면: 넣고, 업데이트, 재귀
#       안 된다면: continue