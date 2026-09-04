class Solution:
    d: dict
    def __init__(self):
        self.d = dict()

    def traverse(self, nums: List[int]):
        if tuple(nums) in self.d:
            return self.d[tuple(nums)]

        n = len(nums)
        if n == 1:
            self.d[tuple(nums)] = nums[0]
            return nums[0]

        scores = []; cur = []

        for i in range(n):
            left = 1; right = 1;
            if i >= 1: left = nums[i-1]
            if i < n - 1: right = nums[i+1]

            cur.append(left * nums[i] * right)

            new_arr = nums[:i] + nums[i+1:]

            scores.append(self.traverse(new_arr))
        ans = 0
        for i in range(n):
            ans = max(ans, scores[i] + cur[i])

        self.d[tuple(nums)] = ans
        return ans

    def maxCoins(self, nums: List[int]) -> int:
        self.traverse(nums)
        
        return self.d[tuple(nums)]

# 되게 신기한 조건이네
# i번째 풍선을 터트리면 nums[i-1] * nums[i] * nums[i+1] 만큼의 점수를 받고,
# 점수들의 합을 최대로 만드는 순서를 찾아라는 건데..

# 1차원으로 생각하면 어떤 정보 하나가 부족하다. 어디서부터 출발한거든, 뭐든 간에.

# DFS가 생각나는 문제긴 하네. 혹시 얘도 반복되는 무언가가 있나?
# 결국 남는 애들이 반복되긴 하네. 근데 이걸 어떻게 DP로 표현하냐의 문제인데...
# DP의 메인은 결국 memoization이잖아? 그러면 memoization만 잘 하면 되는 문제 아니야? 그러면 Hashmap으로 써도 되잖아? 똑같은 O(1)이니까.

# 그러면 key는 무엇이 될까. 현재 남은 수들의 tuple이 되겠네.