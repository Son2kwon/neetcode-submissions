class Solution:
    def reverse(self, x: int) -> int:
        ans = []; flag = False

        for c in str(x)[::-1]:
            if c == "-": 
                flag = True
                continue

            ans.append(c)

        ans = int(''.join(ans))

        if flag: ans = ans * -1

        if ans < pow(-2, 31) or ans > pow(2, 31) - 1:
            ans = 0

        return ans

        

        

# 32비트 정수를 벗어난 애들을 사용하지 않고, 문제를 풀어라

# 13 = 0000 1101
# 31 = 0001 1111

# 123 = 0000 0111 1011
# 321 = 0001 0100 0001

# 딱히 bit의 규칙성이 보이는 것도 아니고... 진짜 말 그대로 뒤집어서 처리하는 게 낫나?

# 2^31 - 1  = 0111 1111 1111 1111 1111 1111 1111 .... 1111
# -2^31     = 1000 0000 0000 0000 0000 0000 0000 .... 0000