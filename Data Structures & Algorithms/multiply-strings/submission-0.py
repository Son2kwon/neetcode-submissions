class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
# string을 integer로 바로 옮겨주는 라이브러리 쓰지 마라라는 것도 조건이네
# 애초에 숫자 길이가 200자리라서, integer로 바꾸는 것도 쉽지 않다.

# num1 * num2 = num1 * num2/2 * 2