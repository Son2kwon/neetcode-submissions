class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int); n = len(nums)

        for i in range(0, n):
            print(d)
            print(nums[i])
            t = target - nums[i]

            if nums[i] in d:
                return [d[nums[i]], i]
            
            d[t] = i
        
# 26.06.12 복습

# target - nums[i] = (우리가 필요한 숫자) 이므로 이 내용을 딕셔너리에 넣는다.
#   key: 필요한 숫자, value: 인덱스

# Time Complexity: O(n)
# Space Complexity: O(n)