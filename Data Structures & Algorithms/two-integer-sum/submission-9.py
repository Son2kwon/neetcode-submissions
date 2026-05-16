class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dictionary: dict[int, int] = {}

        for i in range (0, n):
            if target - nums[i] in dictionary:
                return [dictionary[target-nums[i]], i]
            else:
                dictionary[nums[i]] = i


# Time Complexity: O(n)
# Space Complexity: O(n)