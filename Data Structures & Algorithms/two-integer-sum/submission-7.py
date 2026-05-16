class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dictionary: {int, int} = {}

        for i in range(0, n):
            dictionary[nums[i]] = i

        for i in range(0, n):
            cur = target - nums[i]

            if cur in dictionary and dictionary[cur] != i:
                return [min(dictionary[cur], i), max(dictionary[cur], i)]