class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        DP = [[0 for _ in range(3)] for _ in range(n)]

        DP[0][0] = -prices[0]

        for i in range(1, n):
                DP[i][0] = max(DP[i-1][0], DP[i-1][1] - prices[i])
                DP[i][1] = max(DP[i-1][1], DP[i-1][2])
                DP[i][2] = DP[i-1][0] + prices[i]

        return max(DP[-1][0], max(DP[-1][1], DP[-1][2]))

# 무엇을 구하는가? max_profit
# 쌓을 때 무엇이 변하는가? 각 날의 값
# 다음 결정에 과거의 뭘 알아야 하는가? 과거의 max_profit을 알아야 비교해서 넣을 수 있음

# 상태 = 주식을 들고 있으면 0 / 자유로우면 1 / 오늘 팔았는지 2
# DP[i][상태] = ith day의 장 마감 때의 상태에 따른 max_profit

# 오늘 주식을 들고 있다면: max(어제도 들고 있었음, 어제 자유로움 + 오늘 삼)
# 오늘 자유롭다면: 어제 자유로움, 어제 팔았음
# 오늘 팔았다면: 어제 들고 있던 주식을 팔아서 이익 실현

# DP[i][0] = max(DP[i-1][0], DP[i-1][1] - prices[i])
# DP[i][1] = max(DP[i-1][1], DP[i-1][2])
# DP[i][2] = DP[i-1][0] + prices[i]