class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0; right = len(nums) - 1;

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return -1

        
        


# target이 어디에 들어있는가를 확정짓자
# nums[left] <= nums[mid] 라면, left ~ mid는 완벽 정렬
#   nums[left] <= target <= nums[mid] 라면 right = mid - 1
#   아니라면 left = mid + 1

# nums[mid] >= nums[right] 라면, mid~right은 완벽 정렬
#   nums[mid] <= target <= nums[right] 라면 left = mid + 1
#   아니라면 right = mid - 1

# Time Complexity: O(log n)
# Space Complexity: O(1)