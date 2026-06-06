class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        flag = True

        while slow != fast or flag:
            slow = nums[slow]
            fast = nums[nums[fast]]
            flag = False

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
        

# 배열을 Linked List 처럼 본다면,
#   배열의 인덱스: 노드 / 배열의 값: next