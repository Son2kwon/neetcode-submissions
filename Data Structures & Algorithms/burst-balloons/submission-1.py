class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        DP = [[0 for _ in range(n)] for _ in range(n)]
        
        for length in range (1, n-1):
            for i in range(1, n-length):
                j = i + length - 1

                for k in range(i, j+1):
                    DP[i][j] = max(DP[i][j], DP[i][k-1] + (nums[i-1] * nums[k] * nums[j+1]) + DP[k+1][j])

        return DP[1][-2]



# 마지막에 k번째 풍선을 터트린다면?
# nums[:k-1]이랑 nums[k+1:] 부분은 다 터져있겠지.

# DP로 nums[l:r+1] 부분을 계산해두면, 마지막에 터트리는 애들 가지고 scores를 계산할 수 있구나!

# DP[i][j]: nums[i:j+1] 부분의 점수
# DP[i][j] = max over k in (i ... j) (DP[i][k-1] + (nums[i-1] * nums[k] * nums[j+1]) + DP[k+1][j]) 으로 계산할 수 있겠구만.