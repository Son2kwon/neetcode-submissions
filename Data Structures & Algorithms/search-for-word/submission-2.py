class Solution:
    ans: bool
    def __init__(self):
        self.ans = False

    def find_Candidates(self, i: int, j: int, row: int, col: int) -> List[List[int]]:
        # 맨 윗 줄이라면
        if i == 0:
            # 맨 왼쪽이라면
            if j == 0:
                candidates = [[i, j + 1], [i + 1, j]]
            # 맨 오른쪽이라면
            elif j == col - 1:
                candidates = [[i, j - 1], [i + 1, j]]
            # 중간이라면
            else:
                candidates = [[i, j - 1], [i, j + 1], [i + 1, j]]
        # 맨 아랫 줄이라면
        elif i == row - 1:
            if j == 0:
                candidates = [[i - 1, j], [i, j + 1]]
            elif j == col - 1:
                candidates = [[i - 1, j], [i, j - 1]]
            else:
                candidates = [[i - 1, j], [i, j + 1], [i, j - 1]]
        else:
            if j == 0:
                candidates = [[i, j + 1], [i - 1, j], [i + 1, j]]
            elif j == col - 1:
                candidates = [[i, j - 1], [i - 1, j], [i + 1, j]]
            else:
                candidates = [[i, j - 1], [i, j + 1], [i - 1, j], [i + 1, j]]

        for i, j in candidates:
            if i >= row or j >= col:
                candidates.remove([i, j])
        return candidates

    def backTrack(self, board: List[List[str]], word: str, idx: int, candidates: List[List[int]], used: List[List[bool]]):
        if idx == len(word):
            self.ans = True
            return
        
        for i, j in candidates:
            print(i, j)
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
            for j in range(0, col):
                if word[0] == board[i][j]:
                    used[i][j] = True
                    candidates = self.find_Candidates(i, j, row, col)
                    print(i, j, candidates)                    
                    self.backTrack(board, word, 1, candidates, used)
                    used[i][j] = False

        return self.ans
        
# 이 문제를 Backtracking으로 풀려면..
# 시작점을 잡고
# 상하좌우를 살펴보고 있으면 다음 단계로
# 없으면 가지치기

# 기존에 사용했던 것을 또 쓰면 안 되니까.. used 라는 변수를 사용할까?