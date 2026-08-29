class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums); flag = total + target

        if flag % 2 != 0 or flag < 0:
            return 0

        p = flag // 2

        DP = [0 for _ in range(p + 1)]
        DP[0] = 1

        for num in nums:
            for i in range(p, num-1, -1):
                DP[i] += DP[i-num]

        return DP[p]

# +를 붙인 원소들의 합 = P
# -를 붙인 원소들의 합 = N
# P - N = target
# P + N = total
# 따라서 2P = (target + total)

# (target + total) < 0 or (target + total) == 홀수: return 0
# P = (target + total) // 2 이므로 부분집합의 합을 P로 만들면 됨.
# DP[i]: subset의 원소들의 합을 i로 만드는 경우의 수
# DP[i] += DP[i - num]