class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        ans = [0 for _ in range(len(num1) + len(num2))]

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                cur = int(num1[i]) * int(num2[j])
                idx = 0
                while cur > 0:
                    ans[i + j + 1 - idx] += (cur % 10)
                    cur //= 10
                    idx += 1

        r = 0
        for i in range(len(ans) - 1, -1, -1):
            ans[i] += r
            r = ans[i] // 10
            ans[i] %= 10

        returnValue = "".join(map(str, ans)).lstrip("0")

        if returnValue == "": return "0"
        else: return returnValue

        
# num1[i] * num2[j]는 최종 답의 (i + j)번째 칸에 들어가겠지, 두 자리가 된다면 (i + j - 1)번째 칸까지
# 크기 (m+n)짜리 배열 하나를 만들고, 모든 (i,j) 쌍의 곱을 그 자리에 누적한다면
#   sum이라는 함수가 필요 없어지지
# 자리 올림은 언제하나? 전부 누적한 다음에 마지막에 한 번


# 1111 222
# 2222 + 22220 + 222200
# [0 0 0 0 0 0]