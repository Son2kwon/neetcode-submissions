class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [0 for _ in range(n)]

        for i in range(n):
            cur = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    cur = max(DP[j], cur)

            DP[i] = cur + 1

        return max(DP)



# nums = [9,1,4,2,3,3,7]
# DP = [1, 1, 2, 2, 3, 3, 4]