class Solution:
    ans: List[List[int]]

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], target: int, cur: List[int], cur_sum: int, idx: int):
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue

            cur_sum += nums[i]
            cur.append(nums[i])
            
            if cur_sum > target:
                cur.pop()
                break
            elif cur_sum < target:
                self.backTrack(nums, target, cur, cur_sum, i + 1)
            elif cur_sum == target:
                self.ans.append(cur.copy())
            

            cur_sum -= nums[i]
            cur.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        t = []
        candidates.sort()
        self.backTrack(candidates, target, t, 0, 0)

        return self.ans

# 어제는 얼마든지 쓸 수 있다고 했지만, 오늘은 그냥 정해져 있다.
# 그러면 사실 더 쉽지 않나..? 다음 인덱스부터 검사한다는 마인드로 하면 뭐...
# 저번 문제는 각 숫자가 unique했는데, 이번 건 unique하지 않아서 생기는 문제가 있구나..

# Test Case 중에서 엄청난 입력이 있었다. 1부터 30까지 3번, 1부터 10까지 1번의 입력
# 시간 제한이 떴는데, 그러면 이건 지수 시간을 벗어나야 될 것 같은데...

# counter를 사용한다면...
#   가장 작은 숫자부터 시작한다면...

# 너무 어려워 호시노 도와줘...