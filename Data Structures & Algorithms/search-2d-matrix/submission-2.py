class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0; bottom = len(matrix) - 1;
        left = 0; right = len(matrix[0]) - 1;
        row = 0;

        while top <= bottom:
            mid = (top + bottom) // 2
            print(top, mid, bottom)

            # 찾은 경우
            if matrix[mid][0] == target:
                return True
            
            # 못 찾았는데, 찾아야 하는 row가 mid 일 때
            elif matrix[mid][0] < target and matrix[mid][right] >= target:
                row = mid
                break

            # 일반적인 이진 탐색
            elif matrix[mid][0] > target:
                bottom = mid - 1
            
            elif matrix[mid][0] < target:
                top = mid + 1

        while left <= right:
            mid = (left + right) // 2
            print(row, left, mid, right)

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            
        return False
            
        

# 2차원으로 Binary Search 하는 건 또 처음이네
# row에서 찾는 건 문제가 없는데, column은 좀 문제가 되네.
# matrix[i][0] 의 값은 matrix[i-1]의 모든 값보다 크거나 같다.
#   이걸 기준으로 한 칸씩 옮긴다면 찾을 수는 있겠지만, log 시간으로 들어오지 못함
