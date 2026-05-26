class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]; n = len(heights)
        stack = [];
        right = [n] * n; left = [0] * n
        

        for i in range(0, n):
            cur = heights[i]
            while stack and heights[stack[-1]] > cur:
                right[stack[-1]] = i
                stack.pop()
            
            stack.append(i)

        for i in range(n-1, -1, -1):
            cur = heights[i]
            while stack and heights[stack[-1]] > cur:
                left[stack[-1]] = i
                stack.pop()

            stack.append(i)

        ans = 0

        for i, h in enumerate(heights):
            ans = max(ans, h * (right[i] - left[i] - 1))

        return ans

            


# 이 문제를 어디선가 봤는데.. Leetcode에서 이미 풀어봤던 문제구나

# Monotonic stack을 활용해서 Next Smallest Number를 찾기
#   각 heights를 기준으로, left와 right 얼마나 갈 수 있는 지 계산
