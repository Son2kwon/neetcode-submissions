class Solution:
    ans: List[List[int]]

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], cur: List[int], depth: int, idx: int):
        n = len(nums)

        if depth == n:
            if cur not in self.ans:
                self.ans.append(cur.copy())
            return
        
        for i in range(idx, n):
            if i > idx and nums[i] == nums[i-1]:
                continue

            cur.append(nums[i])
            self.backTrack(nums, cur, depth + 1, i + 1)
            cur.pop()
            self.backTrack(nums, cur, depth + 1, i + 1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backTrack(nums, [], 0, 0)
        return self.ans

# 또 subsets인데, 같은 숫자가 들어가도 된다.
# 어제 호시노가 알려준 것에 따르면, subset은 순서가 중요하지 않다 -> 앞으로만 간다 -> idx 사용

# 만약 모든 값들이 unique 했다면 이 코드로도 풀렸을텐데, 중복인 애들이 있다
#   어라? 이거 저번에 풀었던 문제..?

# 중복인 애들이 있어서 [1, _, 2] 랑 [_, 1, 2]랑 구분이 안 된다.