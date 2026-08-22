class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums); half = total // 2; n = len(nums);
        DP = [False for _ in range(half + 1)]; DP[0] = True
        if total % 2 != 0: return False

        for i in range(n):
            if nums[i] > half: return False

        # 여기까지 하면 nums의 합은 짝수이고, 모든 수는 half보다 작음

        for num in nums:
            for i in range(half, num-1, -1):
                DP[i] = DP[i] or DP[i - num]

        return DP[-1]

        

# 얘도 비슷한 문제를 풀었던 것 같은데... DFS로는 너무 쉬워보이는데 2^n 시간은 TLE가 뜨겠지
# nums.length는 100까지 가능인데 nums[i]가 50까지인 거 보면 중복인 것도 생각해야겠네
# 숫자를 인덱스로 쓰는 방법도 못 쓰겠다

# 일단 전체 합이 짝수여야 가능하고,
# 3 37 -> 이렇게 주어지면 안 되니까.. 실제로 뭔가를 더 짜긴 해야겠다.

# half = (전체 합) / 2 도 써야 할 것 같은디
# 일단 모든 숫자가 half보다 작아야 하지.

# DP[i]: 합이 i인 부분집합을 만들 수 있는가?
# DP[i] = DP[i] or DP[i - num]

# return all(DP)

# 1 2 3 4 -> total = 10, half = 5
# DP = [F F F F]

# 1 2 3 4 5 6 7 -> total = 28, half = 14
# DP = [F F F F F F F]