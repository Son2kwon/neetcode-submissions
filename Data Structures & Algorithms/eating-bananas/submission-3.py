class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1; right = max(piles);
        k = 0; ans = 1000000000

        while left <= right:
            k = left + (right - left) // 2

            count = 0

            for i in piles:
                count += math.ceil(i / k)

            # print(left, right, count, k)
            
            if count <= h:
                ans = min(ans, k)
                right = k - 1
            else:
                left = k + 1

        
        return ans
            

        
# 이 문제가 이진 탐색과 무슨 관련이 있죠..?
# 배열이 정렬되어 있다면, k = piles[i]일 때, i 이전의 모든 pile에 대해 걸리는 시간은 1
#   이후의 것들은 몫
# log n 번의 수행 안에 O(n + n/2 + n/4 + ...) = O(n)
# 따라서 time Complexity: O(n log n)