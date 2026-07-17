class Solution:
    ans: List[List[int]]

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], target: int, cur: List[int], cur_sum: int, idx: int):
        for i in range(idx, len(nums)):
            cur.append(nums[i])
            cur_sum += nums[i]

            if cur_sum < target:
                self.backTrack(nums, target, cur, cur_sum, i)

            elif cur_sum == target:
                self.ans.append(cur.copy())

            cur.pop()
            cur_sum -= nums[i]
            

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        t = []
        self.backTrack(nums, target, t , 0, 0)

        return self.ans
        
# target을 만드는 조합을 만들어라 + 같은 숫자는 여러번 나올 수 있다.
# 그냥 조합을 하는 거면 오히려 쉽게 하겠는데, 같은 숫자가 여러 번 나올 수 있다는 조건이..

# 재귀마다 0번째부터 출발 (i = 0)
#   sum += nums[i]
#   if sum > target: 빠져 나옴
#   if sum == target: ans에 업데이트 하고 빠져나옴
#   if sum < target: i += 1

# 파이썬에서 객체에 따라 call by reference, call by value 가 달라진다.