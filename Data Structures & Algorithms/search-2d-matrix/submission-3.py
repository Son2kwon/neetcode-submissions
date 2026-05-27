class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix); row = len(matrix[0])
        left = 0; right = row * col - 1
        

        while left <= right:
            mid = left + (right - left) // 2

            i = mid // row; j = mid % row

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            
        return False
            
        

# 2차원 배열도 결국은 1차원 배열의 배열이다.
# 1차원 배열 index와 2차원 배열 index 변환 수식
#   [i][j] => (i * row) + j
#   n => [n / row][n % row]

# Time Complexity: O(log m + log n = log(m * n))
# Space Complexity: O(1)