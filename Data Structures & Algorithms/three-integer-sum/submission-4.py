class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(); n = len(nums)
        ans = []

        for i in range(0, n):
            left = i + 1; right = n - 1;
            target = -nums[i]

            while left < right:
                val = nums[left] + nums[right]

                if val == target:
                    cur = [nums[left], nums[right], nums[i]]
                    if cur not in ans:
                        ans.append([nums[left], nums[right], nums[i]])
                    left += 1

                elif val < target: 
                    left += 1
                else:
                    right -= 1

        return ans


# 모든 조합을 다 훑는 방법도 있는데, 그건 O(n^3)으로 가니까 쓰면 안 돼.
# Sorting 후, 기준값을 정한다. 그 기준값보다 오른쪽 배열에서 조합을 찾는다.
# Time Complexity: O(n^2)
# Space Complexity: O(n)