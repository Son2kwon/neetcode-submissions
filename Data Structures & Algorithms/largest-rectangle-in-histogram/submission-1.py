class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]; n = len(heights)
        stack = []; length = [n] * n

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                tmp = stack[-1]
                stack.pop()
                length[tmp] = i - stack[-1] - 1
                
            
            stack.append(i)

        ans = 0

        for i, h in enumerate(heights):
            ans = max(ans, h * length[i])

        return ans

            


# 이 문제를 어디선가 봤는데.. Leetcode에서 이미 풀어봤던 문제구나

# Monotonic stack을 활용해서 Next Smallest Number를 찾기
#   각 heights를 기준으로, left와 right 얼마나 갈 수 있는 지 계산
#   Left bound는 pop 하고 stack[-1], Right bound는 자기를 밀어낸 i

# Time Complexity: O(n)
# Space Complexity: O(n)
