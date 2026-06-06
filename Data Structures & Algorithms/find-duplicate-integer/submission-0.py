class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort(); n = len(nums);

        for i in range(0, n):
            if nums[i] == nums[i+1]:
                return nums[i]
        
# 그냥 마음 편하게 hash table 쓰려고 했는데, O(1) space로 풀라 그러니 원...
# Linked List가 아니라 그냥 list니까, sorted 한 다음에 다음 숫자랑 같냐로 풀면 시간 O(n log n), 공간 O(1)