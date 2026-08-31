class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1); n2 = len(s2); n3 = len(s3);
        if n1 + n2 != n3:
            return False
        DP = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        DP[0][0] = True
        for i in range(1, n1 + 1):
            DP[i][0] = DP[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, n2 + 1):
            DP[0][j] = DP[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                DP[i][j] = (DP[i-1][j] and s1[i-1] == s3[i+j-1]) \
                        or (DP[i][j-1] and s2[j-1] == s3[i+j-1])

        return DP[-1][-1]



#  오우아...

# s1을 쪼개고, s2를 쪼개서 그 조합으로 s3를 만들 수 있는가?
# 이건 또 DP로 어떻게 접근을 한담...

# DP[i][j]: s1[0..i], s2[0...j] 가지고 s3[0...i+j]를 만들 수 있는가?
# (0,0)에서 출발해서 오른쪽으로 가면 s2 사용, 아래로 가면 s1 사용
# DP[i][j] = DP[i-1][j] or DP[i][j-1]
# return DP[-1][-1]