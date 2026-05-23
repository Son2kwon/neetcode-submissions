class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []; left = 0; right = k - 1; max_idx = 0; n = len(nums)

        for i in range(0, k):
            if nums[i] > nums[max_idx]:
                max_idx = i

        while right < n:
            ans.append(nums[max_idx])

            left += 1
            right += 1
            # 새로운 max 값이 들어온 경우
            if right < n and nums[max_idx] < nums[right]:
                max_idx = right
            # max_idx가 left를 벗어난 경우
            elif right < n and max_idx < left:
                max_idx = left
                for i in range(left, right + 1):
                    if nums[i] > nums[max_idx]:
                        max_idx = i


        return ans
            


# 마지막치고는 너무 싱거운데..?
# 