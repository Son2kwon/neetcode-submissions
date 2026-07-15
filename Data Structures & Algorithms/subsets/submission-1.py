class Solution:
    ans: List[List[int]]

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], status: List[bool], depth: int):
        print(depth)
        print(status)
        print()
        if depth == len(nums):
            cur = []
            for i, v in enumerate(status):
                if v:
                    cur.append(nums[i])

            self.ans.append(cur)

            return

        self.backTrack(nums, status, depth + 1)
        
        status[depth] = True

        self.backTrack(nums, status, depth + 1)

        status[depth] = False

    def subsets(self, nums: List[int]) -> List[List[int]]:
        status = [False] * len(nums)
        self.backTrack(nums, status, 0)

        return self.ans

# 이제는 한 단원의 시작이 Easy가 아니라 Medium이네..

# 그래도 백트래킹의 가장 기본적인 문제가 나왔네.