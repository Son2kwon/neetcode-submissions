class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits); r = 0;

        if int(digits[-1]) + 1 >= 10:
            r = 1
        else:
            digits[-1] = int(digits[-1]) + 1

        for i in range(n-1, -1, -1):
            cur = int(digits[i]) + r

            if cur >= 10:
                r = 1; 
                cur %= 10
            else:
                r = 0

            digits[i] = cur

        if r == 1:
            digits = [1] + digits

        return digits

# 뭐야 그냥 1 더하라는 거잖아.
# 숫자로 변환한다음에 1 더하고 list화 시키면 되긴 하는데...

# 그냥 마지막 숫자부터 1 더하고, 하나씩 올려볼까?