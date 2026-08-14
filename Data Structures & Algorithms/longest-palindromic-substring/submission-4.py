class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        DP = [[True for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i >= j: continue

                DP[i][j] = False
                break

        for i in range(n-1, -1, -1):
            for j in range(n):
                if i >= j: continue

                DP[i][j] = (s[i] == s[j]) and DP[i+1][j-1]

        l = 0; r = 0;

        for i in range(n):
            for j in range(n):
                if i > j: continue

                if DP[i][j] and (r - l) < (j - i):
                    l = i; r = j

        return s[l:r+1]
        
# 그래도 DP에 있는 문제니까 DP로 풀어보자

# DP[i][j] = s[i:j+1] 이 회문인가?
# if s[i] == s[j]:
#   DP[i][j] = DP[i+1][j-1]

"""
ababd

[T F T F F]
[F T F T F]
[F F T F F]
[F F F T F]
[F F F F T]

bb

[T F]
[F T]

i > j 인 부분은 안 씀
i <= j인 부분부터 씀
"""
