class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount + 1; m = len(coins)

        DP = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            DP[0][i] = 1

        for i in range(1, n):
            for j in range(m):
                if i >= coins[j]:
                    DP[i][j] += DP[i-coins[j]][j]
                else:
                    DP[i][j] = 0

                if j >= 1: DP[i][j] += DP[i][j-1]

        return DP[-1][-1]

# 이번엔 거기까지 도달할 수 있는 경우의 수를 출력하라는 말이네..

# 현재의 개수를 알기 위해 (i-coin)을 만드는 경우의 수가 필요함
# DP[i]: i라는 price를 만들 때의 경우의 수 -> 축이 부족하다

# DP[i][j]: i라는 price를 만들기 위해 coins[j]를 포함했을 때의 조합 수

"""
    1 2 3
0: [1 1 1]
1: [1 1 1]
2: [1 2 2]
3: [1 2 3]
4: [1 3 4]
"""