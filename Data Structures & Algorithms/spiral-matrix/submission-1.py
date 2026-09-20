class Solution:
    ans: List[int]

    def __init__(self):
        self.ans = []

    def printCurRound(self, matrix: List[List[int]], row_start: int, row_end: int, col_start: int, col_end: int):
        if row_start >= row_end or col_start >= col_end:
            return

        print(row_start, row_end, col_start, col_end)

        # col의 변화만 남음
        if row_start == row_end - 1:
            for i in range(col_start, col_end):
                self.ans.append(matrix[row_start][i])
            return

        # row의 변화만 남음
        elif col_start == col_end - 1:
            for i in range(row_start, row_end):
                self.ans.append(matrix[i][col_start])
            return

        for i in range(col_start, col_end):
            self.ans.append(matrix[row_start][i])

        for i in range(row_start + 1, row_end):
            self.ans.append(matrix[i][col_end - 1])

        for i in range(col_end - 2, col_start - 1, -1):
            self.ans.append(matrix[row_end - 1][i])

        for i in range(row_end - 2, row_start, -1):
            self.ans.append(matrix[i][col_start])

        self.printCurRound(matrix, row_start + 1, row_end - 1, col_start + 1, col_end - 1)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.printCurRound(matrix, 0, len(matrix), 0, len(matrix[0]))

        return self.ans

# 빙글빙글 도는 순서를 출력하라는건데
# 그냥 하나씩 해본다면...
# row = 0, col = 0 ~ n-1 까지 돌고
# row = 0 ~ n-1, col = n-1 까지 돌고
# row = n-1, col = n-1 ~ 0 까지 돌고
# row = n-1 ~ 1, col = 0 까지 돌고

# 재귀적으로 풀면 될 것 같은데?
# (0 ~ n-1), (1 ~ n-2), (2 ~ n-3), ... 이 안에서 돈다고 생각하면 될 것 같은데?
# 음... 코드 자체도 문제긴 한데, TLE가 뜨긴 하네.

# 힌트1: Try to simulate the process. Starting from the outermost boundaries and moving inward. Can you determine an efficient way to implement this?
# 결국 내가 생각한 거랑 똑같네. 
# 일단 정사각형은 되는데, 직사각형의 base condition은 뭐지?