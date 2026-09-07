class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums); count = 0
        l = 0; r = 0;

        while r < n - 1:
            nxt = 0

            for j in range(l, r+1):
                nxt = max(nxt, j + nums[j])

            l = r + 1; r = nxt

            count += 1


        return count

        
        

# 나는 또 다시 점프를 해야해...
# 이전에는 가능성만 봤다면 이번엔 점프의 최솟값이네, 대신 무조건 도달할 수 있는거고

# 처음부터 출발해서 뛸 수 있는 칸 안에서 최대값을 골라서 뛴다면..? 진짜 greedy긴 한데

# 힌트1: BF는 exponential이니까 greedy가 도움이 될 수도..?
# 힌트2: l, r 2개의 Index를 사용해서 그 사이에 가장 멀리 갈 수 있는 칸을 찾자
# 뭐야, 결국 위에 생각했던 거랑 비슷하네.

# 힌트3: l, r 2개의 포인터를 계산 후에, l = r + 1, r = 가장 멀리 갈 수 있는 index로 계산 한 다음에 다시 반복
# 힌트4: 저 방법을 사용해서 세면 가장 적은 steps