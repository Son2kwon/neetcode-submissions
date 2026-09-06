class Solution:
    def traverse(self, s: str, p: str, i: int, j: int, DP: List[List[int]]) -> bool:
        if j == len(p):
            return i == len(s)

        if DP[i][j] != -1:
            return DP[i][j] == 1

        match = i < len(s) and (p[j] == "." or s[i] == p[j])

        if j <= len(p) - 2 and p[j+1] == "*":
            cur = []
            if match:
                cur.append(self.traverse(s, p, i, j+2, DP))
                cur.append(self.traverse(s, p, i+1, j, DP))
            else:
                cur.append(self.traverse(s, p, i, j+2, DP))
            DP[i][j] = any(cur)
            return DP[i][j]

        elif match:
            DP[i][j] = self.traverse(s, p, i+1, j+1, DP)
            return DP[i][j]
        
        return False
        

    def isMatch(self, s: str, p: str) -> bool:
        DP = [[-1 for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        return self.traverse(s, p, 0, 0, DP)

# 정규표현식인가...
# p만 가지고 1차원 DP를 하기엔 s의 index 정보가 부족하니까

# DP[i][j]: s[0:i+1]이 p[0:j+1]의 표현식과 맞는가?
# if p[j] == "*": DP[i][j] = True
# elif p[j] == "." and s[i] != "": DP[i][j] = True
# elif p[j] == s[i]: DP[i][j] = DP[i-1][j-1]

# 대각선에서만 이동하는데... 이거 인접한 cell에서 오는 정보는 필요 없나?

# 힌트1: recursion and decision tree. *을 만나면 explore different combinations
# 그러면 *을 만나기 전에는 그냥 1차원처럼 하나하나 비교해도 되는거잖아?
# decision tree 그려보니까 뭐 똑같이 반복되는 게 있긴 한데...

# 힌트2: match하거나 "."이 있으면 둘 다 증가. * 라면 skip하거나 i만 증가하거나
# 이전에 봤던 거랑 비슷한데...
# BF로 풀었다 생각했는데 edge case가 있네

# 힌트3: BF는 exponential 한데 최적화 가능?
# 딱 고민중인 지점이네..