class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0; right = len(nums) - 1; mid = 0;
        k = 0; ans = -1

        # 최솟값 찾기
        while left < right:
            k = left + (right - left) // 2

            if nums[k] > nums[right]:
                left = k + 1
            else:
                right = k

        k = left

        left = 0; right = k-1;

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = k; right = len(nums) - 1;
        print(left, right)

        while left <= right:
            mid = left + (right - left) // 2
            

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
        

# 똑같은 문제라 생각했는데, 이번엔 target을 찾는 문제네
# (0 ~ k) > (k+1 ~ n-1) 인 상황
# muns[mid] > target 이면
#   1) left right이 같은 범위에 있다 -> 일반적인 BST -> right = mid
#   2) 다른 범위에 있다 -> left = mid + 1
# nums[mid] < target 이면
#   1) 같은 범위에 있다 -> 일반적인 BST -> left = mid + 1
#   2) 다른 범위에 있다 -> right = mid

# 위에 처럼 풀어봤는데 안 풀리네...
# 이진 탐색 3번으로 풀리긴 하겠다
#   1) 이전에 풀었던 가장 작은 값을 찾는다. nums[k+1]
#   2) 0 ~ k 사이에서 이진 탐색
#   #) k+1 ~ n-1 사이에서 이진 탐색