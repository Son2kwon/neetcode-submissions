class Solution:
    def quickSelect(self, nums: List[int], left: int, right: int, k: int) -> int:
        if left == right:
            return nums[left]
        # pivot 설정
        pivot = (left + right) // 2
        # pivot을 right와 swap
        nums[right], nums[pivot] = nums[pivot], nums[right]
        # l = left, r = right - 1, pivot = right 설정
        l = left; r = right - 1; pivot = right
        # l < r일 동안에...
        while l <= r:
            # 내림차순으로 정리할 것이기 때문에, pivot의 왼쪽에는 더 큰 값이 나와야 함 -> nums[l] < nums[pivot] 확인
            if nums[l] > nums[pivot]:
                l += 1
                continue
            # 반대로 pivot의 오른쪽에는 더 작은 값이 나와야 함 -> nums[r] >= nums[pivot] 확인
            if nums[r] <= nums[pivot]:
                r -= 1
                continue
            # l과 r이 못 움직일 때 -> nums[l] >= nums[pivot] and nums[r] < nums[pivot]
            if nums[l] <= nums[pivot] and nums[r] > nums[pivot]:
                nums[l], nums[r] = nums[r], nums[l]
                continue

        # 비교를 다 했으면, l과 pivot을 swap
        nums[l], nums[pivot] = nums[pivot], nums[l]

        if l == k - 1:
            return nums[l]
        elif l < k - 1:
            return self.quickSelect(nums, l + 1, right, k)
        else:
            return self.quickSelect(nums, left, l, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)