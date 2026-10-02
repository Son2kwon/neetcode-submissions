class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0; bit_length = 32; carry = 0

        for i in range(0, bit_length):
            x = (a >> i) & 1; y = (b >> i) & 1
            s = x ^ y ^ carry
            carry = (x & y) | (y & carry) | (carry & x)

            ans = ans | (s << i)

        # 음수라면...
        if (ans >> (bit_length - 1)) & 1 == 1:
            mask = 0xFFFFFFFF
            ans = ~(ans ^ mask)

        return ans

# sum = a XOR b XOR c
# carry = (a AND b) or (b AND c) or (c AND a)

# 1. ~x = -x - 1
# 2. x ^ mask = 2^{bit_length} - 1 - x
# let f = x ^ mask = 2^{bit_length} - 1 - x
# then, ~f = -f - 1 = - (2^{bit_length} - 1 - x) - 1 = -2^{bit_length} + x
# ~(x ^ mask) = x - 2^{bit_length}

# 따라서, ans = ans - 2^{bit_length} = ~(ans ^ mask)
# 라는 건데, 이것도 이상하게 나오네...