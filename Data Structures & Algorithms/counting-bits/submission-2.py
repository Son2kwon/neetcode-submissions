class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n + 1)]

        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


# n이 주어지면 0부터 n까지의 수들의 1의 개수를 출력하라

# DP[i] = DP[i >> 1] + (i의 마지막 비트)

# Time Complexity: O(n)
# Space Complexity: O(1)