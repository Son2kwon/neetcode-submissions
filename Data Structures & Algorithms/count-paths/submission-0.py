class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # edge들은 1가지 방법으로 접근할 수 있음
        grid = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]

# 피카츄! 도착했어! 2D DP야!

# 이거 확률과 통계에서 되게 유명한 문제인데.. (m+n)! / m!n! 하는 식으로 풀 수 있지.

# DP로 풀자면, grid[i][j] = grid[i-1][j] + grid[i][j-1] 로 표현할 수 있어.
# 왼쪽 상단부터 오른쪽 하단으로 내려가는 방향인거지. 그래서 i랑 j 모두 0부터 올라가야해.