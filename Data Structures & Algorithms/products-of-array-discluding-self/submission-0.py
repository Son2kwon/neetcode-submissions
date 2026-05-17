class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range (1, n):
            left[i] = left[i - 1] * nums[i]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]

        ans = []

        for i in range(0, n):
            if i == 0:
                ans.append(right[i + 1])
            elif i == n - 1:
                ans.append(left[i - 1])
            else:
                ans.append(left[i - 1] * right[i + 1])

        return ans