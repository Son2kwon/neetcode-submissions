class Solution:
    def recursion(self, s: str, t: str, i: int, j: int, DP: List[List[int]]):
        if j == len(t):
            return 1
        if i == len(s):
            return 0

        if DP[i][j] != -1:
            return DP[i][j]

        a = 0; b = 0;

        if s[i] == t[j]:
            a = self.recursion(s, t, i+1, j+1, DP)
        
        b = self.recursion(s, t, i+1, j, DP)

        DP[i][j] = a + b

        return DP[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        DP = [[-1 for _ in range(len(t))] for _ in range(len(s))]
        return self.recursion(s, t, 0, 0, DP)

# 과거의 완성된 걸 가져와서, 뒤에 같으면 갖다 붙인다 느낌일 것 같은데 개수는 어떻게 세지?
# 대각선의 정보를 가져와서 +1 한다면...

# DP[i][j]: t[i]까지 고려했을 때 만들 수 있는 경우의 수
# if s[j] == t[i]: DP[i][j] = DP[i-1][j] + DP[i][j-1]
# else: DP[i][j] = DP[i][j-1]
# edge case가 존재한다

# 힌트1: 재귀 단계마다 possible decisions를 determine 할 수 있나?
# 힌트2: recursive function의 base condition은 무엇인가?

# 일단 재귀로 풀라는 것 같은데.. 이것도 DP로 접근하는 무언가가 있는건가?
# s[i] == t[j]면 그거 포함하고 재귀 한 번, 빼고 재귀 한 번
# base condition은 j == len(t) 하고 뭐가 더 있는데..

# 힌트3: j가 out of bounds면 return 1, i가 out of bounds면 return 0, 매 재귀마다 sum of both paths를 return. exponential한데 이거 최적화 가능?
# 그림 그려보니까 결국 계속 같은 애들이 나오네. DP로 풀 수 있겠다.

# TLE가 떴는데... 뭐가 문제지