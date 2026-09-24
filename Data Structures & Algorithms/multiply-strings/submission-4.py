class Solution:
    def sum(self, num1: str, num2: str) -> str:
        if len(num1) <= len(num2):
            num1, num2 = num2, num1

        r = 0; returnValue = ""; i = len(num1)-1; j = len(num2)-1;

        while i >= 0 and j >= 0:
            cur = int((num1[i])) + int((num2[j])) + r
            r = cur // 10
            cur %= 10

            returnValue = str(cur) + returnValue
            i -= 1; j -= 1;

        while i >= 0:
            cur = int((num1[i])) + r
            r = cur // 10
            cur %= 10

            returnValue = str(cur) + returnValue
            i -= 1;

        if r != 0: returnValue = str(r) + returnValue

        return returnValue

    def multiplyDigit(self, num1: str, num2: str) -> str:
        r = 0; n = len(num1); returnValue = ""

        for i in range(n-1, -1, -1):
            cur = int(num1[i]) * int(num2) + r
            r = cur // 10; cur %= 10
            returnValue = str(cur) + returnValue

        if r != 0: returnValue = str(r) + returnValue

        return returnValue

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        ans = ""; zeros = ""

        for i in range(len(num2)-1, -1, -1):
            cur = self.multiplyDigit(num1, num2[i]) + zeros
            ans = self.sum(ans, cur)
            zeros = zeros + "0"
        

        return ans

#  222
# 2220
# 2442

# string을 integer로 바로 옮겨주는 라이브러리 쓰지 마라라는 것도 조건이네
# 애초에 숫자 길이가 200자리라서, integer로 바꾸는 것도 쉽지 않다.

# 힌트1: 2개의 string number를 받아 더하는 함수를 만들어라.
# 각 자릿수 곱한 다음에, 그 결과들을 sum에 더하는 느낌으로?