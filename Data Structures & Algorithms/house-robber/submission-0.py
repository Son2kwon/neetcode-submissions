class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] + nums;
        n = len(nums)
        DP = [0 for _ in range(n)]
        DP[1] = nums[1]

        for i in range(2, n):
            DP[i] = max(DP[i - 2] + nums[i], DP[i - 1])

        return DP[n - 1]

# 강도짓을 DP로 해결하라고..? 헉
# 바로 옆 집을 털지 말고 최댓값을 가져오라는건데
# DP[i] = max(DP[i - 2] + nums[i], DP[i - 1])