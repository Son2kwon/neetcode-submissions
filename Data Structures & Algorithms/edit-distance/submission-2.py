class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1); m = len(word2)
        DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            DP[i][0] = i

        for j in range(1, m + 1):
            DP[0][j] = j            

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1

        return DP[-1][-1]

# 저번에 호시노가 알려줬던 것 같은데...

# if word1[i] == word2[j]: DP[i][j] = DP[i-1][j-1]
# else: DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1