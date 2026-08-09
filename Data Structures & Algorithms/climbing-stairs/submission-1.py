class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
            
        DP = [0 for _ in range(n + 1)] 
        DP[0] = 0; DP[1] = 1; DP[2] = 2

        for i in range(3, n + 1):
            DP[i] = DP[i - 2] + DP[i - 1]

        return DP[n]

# Topic이 DP 구만... 잘 못 다루는데
# DP의 대표적인 문제네

# 1개의 계단 -> 1가지
# 2개의 계단 -> 1개의 계단의 경우의 수 + 2칸 한 번에 오름 = 2가지
# 3개의 계단 -> 1칸짜리 + 2칸짜리 = 3가지
# 4개의 계단 -> 2칸짜리 + 3칸짜리 = 5가지
# ...
# n개의 계단 -> DP[n-2] + DP[n-1]