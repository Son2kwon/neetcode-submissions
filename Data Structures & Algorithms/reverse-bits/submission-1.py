class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0; power = 31;

        while n:
            cur = n & 1
            if cur == 1:
                ans = ans | 1 << power
            
            power -= 1
            n = n >> 1

        return ans

# 저걸 그냥 int형으로 입력되나 했는데, 2진수로 입력 되는거구나
# 결국 비트 하나씩 하는 게 좋아보이긴 하네..

# Time Complexity: O(n) -> O(32) = O(1)
# Space Complexity: O(1)