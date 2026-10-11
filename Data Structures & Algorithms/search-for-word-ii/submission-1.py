class Solution:
    ans: List[str]

    def __init__(self):
        self.ans = []

    def findCandidates(self, x: int, y: int, row: int, col: int, visited: List[List[bool]]) -> List[int]:
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        candidates = []

        for dx, dy in delta:
            nx = x + dx; ny = y + dy;
            if 0 <= nx and nx < row and 0 <= ny and ny < col and not visited[nx][ny]:
                candidates.append([nx, ny])

        return candidates

    def traverse(self, board: List[List[str]], x: int, y: int, cur: dict, words: List[str], visited: List[List[bool]]):
        c = board[x][y]; 
        if c not in cur:
            return

        cur = cur[c]
        row = len(board); col = len(board[0])

        if "*" in cur and cur["*"] != -1:
            self.ans.append(words[cur["*"]])
            cur["*"] = -1



        

        visited[x][y] = True

        candidates = self.findCandidates(x, y, row, col, visited)
        for nx, ny in candidates:
            if board[nx][ny] in cur:
                self.traverse(board, nx, ny, cur, words, visited)

        visited[x][y] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d = {}; row = len(board); col = len(board[0])
        for idx, word in enumerate(words):
            cur = d
            for c in word:
                if c not in cur:
                    cur[c] = {}

                cur  = cur[c]

            cur["*"] = idx

        visited = [[False for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if board[i][j] in d:
                    self.traverse(board, i, j, d, words, visited)

        return self.ans

# 모든 단어를 Trie에 넣는다. 끝 노드에 words의 인덱스를 넣는다.
# 격자의 칸마다 Tries의 루트에서부터 DFS를 시작한다.
# 한 칸 이동할 때마다 그 칸 글자가 Trie 노드의 자식에 있으면 그 자식으로 내려가고, 없으면 멈춘다
# 도착한 노드의 idx != -1 이면 결과에 넣고 -1로 바꾼다. 그리고 계속 간다.