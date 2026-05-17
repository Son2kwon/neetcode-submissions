class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        ans[0] = nums[0]

        for i in range(0, n):
            ans[i] = ans[i-1] * nums[i]

        ans[-1] = ans[-2]; suffix = nums[-1]

        for i in range(n-2, 0, -1):
            ans[i] = ans[i-1] * suffix
            suffix *= nums[i]

        ans[0] = suffix

        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)