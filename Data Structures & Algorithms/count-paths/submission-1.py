class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        p = m + n - 1
        DP = [1 for _ in range(p)]

        for i in range(2, p):
            DP[i] = DP[i - 1] * i

        return DP[-1] // (DP[m-1] * DP[n-1])

# ans = (m - n - 2)! / (m - 1)! (n - 1)!
# 근데 permutation 마저도 DP로 구할 수 있다는 거임!