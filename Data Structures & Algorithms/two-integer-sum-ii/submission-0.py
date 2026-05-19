class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0; right = len(numbers) - 1

        while target != numbers[left] + numbers[right]:
            val = numbers[left] + numbers[right]

            if target > val:
                left += 1
            elif target < val:
                right -= 1

        return [left + 1, right + 1]