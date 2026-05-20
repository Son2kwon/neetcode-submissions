class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0; right = len(height) - 1;
        left_max = 0; right_max = 0;
        ans = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1

        return ans

"""
각 높이마다 담을 수 있는 물의 양 계산

어짜피 높이는 min(height[left], height[right])에 종속됨.

현재까지의 left_max와 right_max를 구했다면...

if left_max < right_max:
    left의 값은 left_max에 종속됨.
    ans += left_max - height[left]
    left += 1
else:
    right의 값은 right_max에 종속됨
    ans += right_max - height[right]
    right -= 1

"""
