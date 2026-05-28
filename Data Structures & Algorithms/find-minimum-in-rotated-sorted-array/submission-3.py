class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0; right = len(nums) - 1; mid = 0;

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

        
        
# 사실상 비교해야 할 것은 nums[right]
# nums[mid] > nums[right] 이라면 left = mid + 1
# nums[mid] <= nums[right] 이라면 right = mid