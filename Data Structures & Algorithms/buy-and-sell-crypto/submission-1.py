class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0; right = 0;
        ans = 0; n = len(prices)

        for right in range (0, n):
            if prices[left] < prices[right]:
                ans = max(ans, prices[right] - prices[left])
            else:
                left = right

        return ans




# 결국 투 포인터로 푸는 거였네...
# 

# Time Complexity: O(n^2)
# Space Complexity: O(1)