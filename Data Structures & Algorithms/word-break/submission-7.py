class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s); i = 0; wordSet = set(wordDict)
        DP = [False for _ in range(n)]
        if s[0] in wordSet: DP[0] = True

        for i in range(1, n):
            for j in range(-1, i):
                if (j == -1 or DP[j]) and s[j+1: i+1] in wordSet:
                    DP[i] = True

        print(DP)

        return DP[n-1]




# 1차원 DP로 접근한다면...

# neetcode / neet, code
# DP = [F F F T F F F T] -> 마지막 반환

# applepenapple / apple, pen, ape
# DP = [F F F F T F F T F F F F T]

# catsincars / cats cat sin in car
# DP = [F F T T F T F F T F]

# 이전 True의 index를 저장해두고 (초기값은 0 저장) = x 라 하자
# s[x:i+1] 이 wordDict에 있으면 index 저장, 다음