class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1); n2 = len(text2);

        DP = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i-1] == text2[j-1]:
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])

        return DP[n1][n2]

        

# DP[i][j]: t1의 앞 i 글자와 t2의 앞 j 글자의 LCS
# DP[i][j] = (t1[i] == t2[j]) ? DP[i-1][j-1] + 1 : max(DP[i-1][j], DP[i][j-1])