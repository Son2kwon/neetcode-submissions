class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        maxHere = [float('-inf') for _ in range(n)]
        minHere = [float('-inf') for _ in range(n)]
        DP = [float('-inf') for _ in range(n)]

        maxHere[0] = nums[0]; minHere[0] = nums[0]; DP[0] = nums[0]

        for i in range(1, n):
            tmp_max = maxHere[i-1] * nums[i]; tmp_min = minHere[i-1] * nums[i]
            DP[i] = max(nums[i], max(tmp_max, tmp_min))
            maxHere[i] = max(nums[i], max(tmp_max, tmp_min))
            minHere[i] = min(nums[i], min(tmp_max, tmp_min))

        return max(DP)