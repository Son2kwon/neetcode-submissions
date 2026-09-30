class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0; power = 31;

        while n:
            cur = n & 1
            if cur == 1:
                ans += pow(2, power)
            
            power -= 1
            n = n >> 1

        return ans

# 저걸 그냥 int형으로 입력되나 했는데, 2진수로 입력 되는거구나
# (n & (n - 1)) 이걸로 오른쪽 비트 하나씩 확인하는 걸로 할까?