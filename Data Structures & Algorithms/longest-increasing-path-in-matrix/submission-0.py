class Solution:
    def findCandidates(self, row: int, col: int, row_max: int, col_max: int, matrix: List[List[int]]):
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        candidates = []

        for drow, dcol in delta:
            nrow = drow + row; ncol = dcol + col;
            if 0 <= nrow and nrow < row_max and 0 <= ncol and ncol < col_max and matrix[row][col] < matrix[nrow][ncol]:
                candidates.append([nrow, ncol])

        return candidates
    def traverse(self, DP: List[List[int]], matrix: List[List[int]], row: int, col: int):
        if DP[row][col] != 0:
            return DP[row][col]

        row_max = len(matrix); col_max = len(matrix[0])
        candidates = self.findCandidates(row, col, row_max, col_max, matrix)
        best = 1
        for ni, nj in candidates:
            best = max(best, self.traverse(DP, matrix, ni, nj) + 1)

        DP[row][col] = best
        return DP[row][col]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix); col = len(matrix[0])

        DP = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                self.traverse(DP, matrix, i, j)

        ans = 0
        for i in range(row):
            for j in range(col):
                ans = max(ans, DP[i][j])

        return ans

# 한 cell에 대해서 DP[i][j] = max(DP[i-1]j], DP[i][j+1]) + 1 하면 될 것 같긴 한데
# DP[i][j]: matrix[i][j]를 포함하는 가장 긴 Path 길이
# matrix의 숫자 순서가 뒤죽박죽이라 과거의 cell을 함부로 쓸 수 없다.
# 그냥 DFS 쓰는 게 제일 직관적인디...

# 힌트1: cell을 revisit 하지 않는다 + Brute Force는 모든 cell에서 출발하기 때문에 exponential
# 불필요한 연산을 없앨 수 있는가?

# 이미 한 번 센 cell들은 다시 출발하지 않는다면...

# 힌트2: results of recursive calls와 avoid redundant computation을 위해 memoization

# 결국 DFS를 사용해서 Longest Path를 찾고
# 그 결과를 DP에 저장해뒀다가
# 그 cell에 도착하면 DP의 값을 꺼내서 써라.

# DP[i][j]: matrix[i][j]에서 출발한 Longest Path의 길이
# DP[i][j] = 

"""
[1 1 2]
[3 2 1]
[4 3 2]
"""