class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0; right = len(heights) - 1;
        ans = 0

        while left < right:
            cur = min(heights[left], heights[right]) * (right - left)
            ans = max(ans, cur)
            print(ans, left, right)

            if heights[left] < heights[right]:
                cur_left = heights[left]
                left += 1
                while left < right and heights[left] <= cur_left:
                    left += 1
            else:
                cur_right = heights[right]
                right -= 1
                while left < right and heights[right] <= cur_right:
                    right -= 1

            

        return ans
        

# Monotonic stack 사용하는 느낌인 것 같은데.. 포인터 2개로 풀라고 하니까 뭐...
# Sorting이 안 된 상태로 투 포인터의 사용이라... 어떻게 움직여야 할 지 감이 안 잡히는데
# 원래 Topic을 보면 안 되지만, greedy라는 키워드가 있었으니...
# 가장 왼쪽과 오른쪽을 선택해 둔 다음에 넓이 계산
# left와 right 중, 더 작은 값을 커지도록 옮김
# 반복