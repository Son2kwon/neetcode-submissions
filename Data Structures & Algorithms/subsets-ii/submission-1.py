class Solution:
    ans: List[List[int]]

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], cur: List[int], idx: int):
        n = len(nums)
        
        
        for i in range(idx, n):
            if i > idx and nums[i] == nums[i-1]:
                continue

            cur.append(nums[i])
            self.ans.append(cur.copy())
            self.backTrack(nums, cur, i + 1)
            cur.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans.append([])
        self.backTrack(nums, [], 0)
        return self.ans

