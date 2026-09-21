class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix); col = len(matrix[0])
        zero_row = False; zero_col = False;

        for i in range(row):
            if matrix[i][0] == 0:
                zero_col = True

        for j in range(col):
            if matrix[0][j] == 0:
                zero_row = True

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0

        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0

        if zero_row:
            for j in range(col):
                matrix[0][j] = 0

        if zero_col:
            for i in range(row):
                matrix[i][0] = 0
                


# 0이 있으면 그 칸을 포함하는 row, column을 모두 0으로 설정하라.
# 근데 공간이 O(1)이었으면 좋겠다.

# 그냥 0 만나면 그 row랑 col을 쫙 돌면... exponential 시간이 들겠는데?
# 아, 그리고 바뀐 0이 영향을 안 미치도록 하는 것도 있겠구나...

# 공간을 O(m)으로 한다면, 0의 위치를 저장하는 배열 하나 두고, 그 배열에 해당하는 row랑 col만 0으로 세팅
# 으로 풀어봤으니, 조금 더 풀어보자.

# 힌트1: BF는 엄청 오래 걸린다. updating entrie row and col 대신 row와 col에 해당하는 하나의 변수를 사용한다.
#   0를 만나면 그 row랑 col을 저장해둔다. 다음 0을 만나면 row, col을 업데이트 한다?
# 힌트2: O(m+n) boolean 배열 사용하면 space를 좀 줄일 수 있다. 이거 Optimize할 수 있나?
#   음... 

# 힌트3: topmost row랑 leftmost col 값을 boolean 배열처럼 사용할 수 있지 않을까?
#   0을 만나면, 그 row의 첫번째 값, col의 첫번째 값을 0으로 설정한다.
#   첫번째 row랑 첫번째 col에 대한 처리만 다른 변수로 저장해둔다면...