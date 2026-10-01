class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0; n = len(nums)
        for num in range(n + 1):
            ans = ans ^ num

        for num in nums:
            ans = ans ^ num

        return ans

# O(n) 시간과 O(1) 공간
# 0, n까지 missing number를 찾아라는 건데

# 그냥 n까지의 합을 저장해두고 하나씩 지나가면서 뺀 다음
# 최종 남은 결과만 반환하면 될 것 같은데?

# Time Complexity: O(n)
# Space Complexity: O(1)