class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row = [set() for _ in range (0, 9)]
        hash_col = [set() for _ in range (0, 9)]
        hash_box = [set() for _ in range (0, 9)]

        for y in range(0, 9):
            for x in range(0, 9):
                val = board[y][x]
                if val == ".": continue
                
                box_idx = (y // 3) * 3 + (x // 3)
                if (val in hash_row[y]) or (val in hash_col[x]) or (val in hash_box[box_idx]):
                    return False

                hash_row[y].add(val)
                hash_col[x].add(val)
                hash_box[box_idx].add(val)

        return True

# Time Complexity: O(n^2): 1 <= n <= 9
# Space Complexity: O(n^2): hash 3개 2차원