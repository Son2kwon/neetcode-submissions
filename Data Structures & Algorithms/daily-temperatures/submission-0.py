class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(0, n):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return ans
        
# Next Greatest Number을 찾는 문제네.
# Stack 중에서도 monotonic stack을 활용하면 돼.

# 