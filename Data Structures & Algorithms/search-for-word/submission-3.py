class Solution:
    ans: bool
    def __init__(self):
        self.ans = False

    def find_Candidates(self, i: int, j: int, row: int, col: int) -> List[List[int]]:
        delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        candidates = []
        for di, dj in delta:
            ni = i + di; nj = j + dj;
            if 0 <= ni < row and 0 <= nj < col:
                candidates.append([ni, nj])

        return candidates

    def backTrack(self, board: List[List[str]], word: str, idx: int, candidates: List[List[int]], used: List[List[bool]]):
        if idx == len(word):
            self.ans = True
            return
        
        for i, j in candidates:
            if self.ans:
                return
            if board[i][j] == word[idx] and not used[i][j]:
                used[i][j] = True
                new_candidates = self.find_Candidates(i, j, len(board), len(board[0]))
                self.backTrack(board, word, idx + 1, new_candidates, used)
                used[i][j] = False
                

    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board); col = len(board[0])
        if len(word) > row * col:
            return False

        used = [[False for _ in range(col)] for _ in range(row)]

        for i in range (0, row):
            if self.ans:
                break
            for j in range(0, col):
                if self.ans:
                    break
                if word[0] == board[i][j]:
                    used[i][j] = True
                    candidates = self.find_Candidates(i, j, row, col)                  
                    self.backTrack(board, word, 1, candidates, used)
                    used[i][j] = False

        return self.ans
        
# 이 문제를 Backtracking으로 풀려면..
# 시작점을 잡고
# 상하좌우를 살펴보고 있으면 다음 단계로
# 없으면 가지치기

# 기존에 사용했던 것을 또 쓰면 안 되니까.. used 라는 변수를 사용할까?
