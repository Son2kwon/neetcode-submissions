class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums); i = 0;
        goal = n-1; i = n-2;

        while i >= 0:
            if i + nums[i] >= goal:
                goal = i

            i -= 1

        return goal == 0

        
# 힌트1: brute force는 exponential, 더 나은 방법 없을까? greedy가 도움이 될 것 같은데?
# 누가 모르냐고요 그걸...

# 힌트2: start from last index.
# 이것도 이미 해본 건데...

# 힌트3: 각 반복마다, goal에 도달할 수 있는지 확인한다. 가능하다면, goal을 current index로 update

# 힌트는 약간 DP적인 느낌인데? memoization은 안 하지만.
# goal = n-1이고, i = n-2 일 때, goal에 도달할 수 있으면 goal = n-2, i -= 1

# 힌트4: goal == 0이면 성공, 아니면 실패