class Solution:
    ans: List[List[int]]

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], cur: List[int], used: List[bool], depth: int):
        n = len(nums)
        if depth == n:
            self.ans.append(cur.copy())
            return

        for i in range(0, n):
            if not used[i]:
                cur.append(nums[i])
                used[i] = True
                self.backTrack(nums, cur, used, depth + 1)
                used[i] = False
                cur.pop()
            else:
                continue
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        cur = []

        self.backTrack(nums, cur, used, 0)

        return self.ans


        

# Permutation은 유우-명한 백트래킹 문제임!
# 근데 어떻게 접근을 할거냐...
# 어떻게 보면 제일 처음 풀었던 백트래킹 문제와 비슷하게 접근한다면?

# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# 2랑 3의 위치를 어떻게 바꿀 것인가