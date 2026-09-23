class Solution:
    d: dict
    def __init__(self):
        self.d = dict()

    def binaryExponentiation(self, x: float, n: int) -> float:
        if n == 0: return 1
        elif n == 1: return x
        elif (x, n) in self.d: return self.d[(x, n)]
        elif n % 2 == 0:
            cur = self.binaryExponentiation(x, n//2)
            self.d[(x, n)] = cur * cur
        else:
            cur = self.binaryExponentiation(x, (n-1) // 2)
            self.d[(x, n)] = x * cur * cur

        return self.d[(x, n)]
    def myPow(self, x: float, n: int) -> float:
        ans = 0
        if n < 0: 
            ans = self.binaryExponentiation(x, -n)
            ans = 1 / ans
        else: ans = self.binaryExponentiation(x, n)
        

        return ans

# 그냥 쉽게 넘어가려 했는데..

# Binary Exponentiation
# 소수 계산을 지원하며, 지수가 정수일 때 정확한 계산을 위해 이렇게 함
# x^y가 있을 때
# y가 짝수라면 x^y = {x^(y/2)}^2
# y가 홀수라면 x^y = x * [x^{(y-1)/2}]^2

# 와중에 DP가 도움을 줄 수 있을 것 같은 느낌?

# 만약 지수가 음수라면...