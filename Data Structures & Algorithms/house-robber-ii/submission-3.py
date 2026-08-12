class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        elif n == 2:
            return max(nums[0], nums[1])

        DP_A = [0 for _ in range(n)]; DP_A[0] = nums[0]; DP_A[1] = max(nums[0], nums[1])
        DP_B = [0 for _ in range(n)]; DP_B[1] = nums[1]; DP_B[2] = max(nums[1], nums[2])

        for i in range(2, n - 1):
            DP_A[i] = max(DP_A[i - 2] + nums[i], DP_A[i - 1])

        for i in range(3, n):
            DP_B[i] = max(DP_B[i - 2] + nums[i], DP_B[i - 1])

        return max(DP_A[-2], DP_B[-1])
        

# 함수 이름이 rob은 너무 폭력적인데
# 저번 문제는 쭉 배열되어 있던 건데, 이번엔 원형으로 이어져 있다라는 건가.
# 최적 부분구조 + 겹치는 부분문제 = DP

# 0번째 집 ~ (n - 2)번째 집까지 털기
# 1번째 집 ~ (n - 1)번째 집까지 털기