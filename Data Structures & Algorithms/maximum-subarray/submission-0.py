
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            # 이전 연속합이 음수면 버리고 현재 원소부터 새로 시작
            current_sum = max(num, current_sum + num)
            # 전체 최대 부분합 갱신
            max_sum = max(max_sum, current_sum)
            
        return max_sum
