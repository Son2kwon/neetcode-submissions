class Solution:
    def reverse(self, x: int) -> int:
        ans = 0; flag = False;

        if x < 0:
            flag = True
            x = x * -1

        while x > 0:
            if ans > ((1 << 31) // 10): return 0

            ans = (ans * 10) + (x % 10)
            x //= 10

        if flag: ans *= -1

        return ans

# 뒤집기를 한 자리씩 쌓는 구조
#   매 단계: ans = ans * 10 + (다음 자리)
#   만약 ans가 넘칠 것 같으면 return 0

# return 0의 조건
#   ans > (2^31 // 10) 이면 return 0
#       1. ans가 10자리가 되었는데도 while loop 안에 들어왔다는 건 이미 over 되는 것
#       2. ans가 9자리 일 때, 214,748,364 보다 크면 그 다음에 뭐가 들어와도 over
#       3. ans가 8자리 이하일 때는 검사할 필요도 없음 -> 214,748,364보다 언제나 작음

# Time Complexity: O(x의 자리수) = O(log_10 {x}) -> O(10) = O(1)
# Space Complexity: O(1)