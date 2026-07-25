class Solution:
    ans: List[List[str]]
    col: set
    diags: set
    anti_diags: set

    def __init__(self):
        self.ans = []
        self.col = set()
        self.diags = set()
        self.anti_diags = set()


    def backTrack(self, n: int, depth: int, cur: List[str]):
        if n == depth:
            self.ans.append(cur.copy())
            return

        status = ["." for _ in range(n)]
        for i in range(0, n):
            if i not in self.col and (depth + i) not in self.diags and (depth - i) not in self.anti_diags:
                status[i] = "Q"; cur.append("".join(status))
                self.col.add(i); self.diags.add(depth + i); self.anti_diags.add(depth - i);
                self.backTrack(n, depth + 1, cur)

                status[i] = "."; cur.pop();
                self.col.remove(i); self.diags.remove(depth + i); self.anti_diags.remove(depth - i)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.backTrack(n, 0, [])

        return self.ans

# 결국 N-Queen 문제까지 왔구나...

# if n == depth:
#   ans 업데이트, return

# for i in range(0, n):
#   수평, 수직, 대각선을 확인
#       된다면: 넣고, 업데이트, 재귀
#       안 된다면: continue