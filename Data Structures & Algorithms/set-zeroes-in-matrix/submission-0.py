class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []; row = len(matrix); col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeroes.append([i, j])

        for x, y in zeroes:
            for i in range(row):
                matrix[i][y] = 0
            for j in range(col):
                matrix[x][j] = 0

                
# 0이 있으면 그 칸을 포함하는 row, column을 모두 0으로 설정하라.
# 근데 공간이 O(1)이었으면 좋겠다.

# 그냥 0 만나면 그 row랑 col을 쫙 돌면... exponential 시간이 들겠는데?
# 아, 그리고 바뀐 0이 영향을 안 미치도록 하는 것도 있겠구나...

# 공간을 O(m)으로 한다면, 0의 위치를 저장하는 배열 하나 두고, 그 배열에 해당하는 row랑 col만 0으로 세팅
# 