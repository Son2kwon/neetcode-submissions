class Solution:
    def reverse(self, x: int) -> int:
        ans = 0; flag = False; length = 0

        if x < 0:
            flag = True
            x = x * -1

        while x > 0:
            if length == 9:
                if ans > ((1 << 31) // 10): return 0
                elif ans == ((1 << 31) // 10):
                    if flag and x > 8: return 0
                    elif not flag and x > 9: return 0

            ans = (ans * 10) + (x % 10)
            x //= 10
            length += 1

        if flag: ans *= -1

        return ans

# 뒤집기를 한 자리씩 쌓는 구조
#   매 단계: ans = ans * 10 + (다음 자리)
#   만약 ans가 넘칠 것 같으면 return 0

# return 0의 조건
#   ans의 현재 자리수가 10자리 이상이 되거나,
#   ans가 현재 9자리 숫자이고 214,748,364 보다 크다면 return 0
#   ans가 현재 9자리 숫자이고 214,748,364와 같고, flag == True이고 x > 8이면 return 0
#   ans가 현재 9자리 숫자이고 214,748,364와 같고, flag == False이고 x > 9이면 return 0
#   ans가 현재 9자리 숫자이고 flag == True이면서, 2,147,483,648 보다 클 때,x

# -2,147,483,648 = -2^31
# -2,143,847,412

# 2,147,483,647 = 2^31 - 1
# 