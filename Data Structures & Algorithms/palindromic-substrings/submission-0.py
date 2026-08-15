class Solution:
    def countSubstrings(self, s: str) -> int:
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

        count = 0

        for i in range(n):
            for j in range(n):
                if i > j: continue

                if DP[i][j]: count += 1


        return count

# 또 palindromes 문제야..?
# 저번에 쓴 코드 + True들만 count 하면 금방 풀릴 것 같은데?