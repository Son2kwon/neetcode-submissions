class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(); n = len(nums)
        ans = []

        for a in range(0, n):
            if nums[a] > 0: break
            if a > 0 and nums[a] == nums[a-1]: continue

            left = a + 1; right = n - 1; target = -nums[a];

            while left < right:
                val = nums[left] + nums[right]
                if val < target:
                    left += 1
                elif val > target:
                    right -= 1
                else:
                    ans.append([nums[left], nums[right], nums[a]])

                    cur_left = nums[left]; cur_right = nums[right];

                    while left < right and cur_left == nums[left]:
                        left += 1
                    while left < right and cur_right == nums[right]:
                        right -= 1

        return ans



# 모든 조합을 다 훑는 방법도 있는데, 그건 O(n^3)으로 가니까 쓰면 안 돼.
# Sorting 후, 기준값을 정한다. 그 기준값보다 오른쪽 배열에서 조합을 찾는다.
# Time Complexity: O(n^2)
# Space Complexity: O(n)