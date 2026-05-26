class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums); left = 0; right = n - 1; idx = n // 2;

        while left <= right:
            if nums[idx] == target:
                return idx
            
            elif nums[idx] > target:
                right = idx - 1

            elif nums[idx] < target:
                left = idx + 1
            
            idx = (right + left) // 2

        return -1



# 단순한 binary search의 구현이네. 내가 이걸 실제로 구현한 적이 있던가...