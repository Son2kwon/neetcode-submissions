class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        DP = [-1 for _ in range(amount + 1)]
        
        DP[0] = 0
        for c in coins:
            if c <= amount: DP[c] = 1

        for i in range(1, amount + 1):
            tmp = []
            for c in coins:
                if i < c: continue
                elif DP[i - c] != -1: tmp.append(DP[i - c] + 1)

            if tmp:
                DP[i] = min(tmp)
            else:
                DP[i] = -1
        
        print(DP)
        return DP[-1]

# 어떻게 보면 DP의 가장 대표적인 문제인데..

# i 를 만드는 방법은 coins의 종류에 따라 달라진다.

# 12
# DP = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3]
# coins = [1,5,10] 이라면
# DP[i] = min(DP[i-1], DP[i-5], DP[i-10]) + 1

# coins = [2], amount = 3
# DP = [0, -1, 1, -1]

# coins = [2, 5]
# DP = [0, -1, 1, -1, 2, 1, 3, 2, 4, 3, 2]