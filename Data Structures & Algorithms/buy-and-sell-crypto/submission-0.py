class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range (0, n):
            for j in range (i + 1, n):
                ans = max(prices[j] - prices[i], ans)

        return ans


# 이걸 sliding window로 푼다고..?
# O(n^2)의 문제 해결 방식은 바로 떠오르는데...
# window 크기를 하나씩 넓히면서 순회하면... O(1+2+3+...(n-1)) = O(n^2) 인데
# 일단 이렇게 풀어볼까? sliding window를 사용하면서 풀려면 이 방법 말고는 없는데.
# 아, 첫번째 날을 for start in prices 로 시작한다음에 뒤에 있는 애들을 계산하는 방법도 있네.
# 근데 이것도 O(n^2)인데...

# Sliding window로 안 푼다면...
# for 문 2개 돌리는 방식으로