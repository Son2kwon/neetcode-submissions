class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1. Reverse the matrix vertically
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

        # 2. Transpose the reversed matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 가장 바깥의 부분만 돌리면 되나?
# 뭔가 회전시키는 건 행렬 곱으로 했던 것 같은데..
# 물론 그 회전 행렬은 아니겠지만 말이야.

# 보니까 그냥 한칸씩 움직이는 게 아니라, 그 열 전체를 시계 방향으로 돌리는거고
# 가운데도 똑같이 돌리는거네.

# 힌트1: BF는 O(n^2)의 space를 사용. space 안 쓰는 방법은 없나? observing the positions of the elements before roating and after rotating of the matrix
# row와 col의 값이 뒤바뀌는 그런 상황인 것 같은데?

# row = 0, col = 0 ~ n-1인 애들 -> col = n-1이 되고, row = 0 ~ n-1
# col = n-1, row = 0 ~ n-1인 애들 -> row = n-1 되고, col = 0 ~ n-1
# row = n-1, col = 0 ~ n-1인 애들 -> col = 0 되고, row = 0 ~ n-1
# col = 0, row = 0 ~ n-1인 애들 -> row = 0 되고, col= 0 ~ n-1

# 안쪽도 돌려야하니까 재귀로

# 힌트2: Reverse the matrix vertically -> Transpose the reversed matrix
# 그냥 아싸리 절반을 잘라서 reverse 하고, transpose를 하면 된다.