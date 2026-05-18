class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = set()

        # Row 검색
        for row in board:
            for i in row:
                if i == ".": continue
                elif i in numbers: return False
                else: numbers.add(i)

            numbers = set()

        # Col 검색
        for i in range (0, 9):
            for j in range (0, 9):
                if board[j][i] == ".": continue
                elif board[j][i] in numbers: return False
                else: numbers.add(board[j][i])

            numbers = set()

        # Box 검색
        for i in range (0, 9, 3):
            for j in range (0, 9, 3):
                print(i, j)
                min_col = (i // 3) * 3; max_col = min_col + 3
                min_row = (j // 3) * 3; max_row = min_row + 3
                print(min_col, max_col, min_row, max_row)

                for y in range (min_col, max_col):
                    for x in range (min_row, max_row):
                        if board[y][x] == ".": continue
                        elif board[y][x] in numbers: return False
                        else: numbers.add(board[y][x])

                numbers = set()

        return True
                

                
            

# Row 검색 1번
# Col 검색 1번
# 칸 검색 1번