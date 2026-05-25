class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = []; n = len(position)

        lst = sorted(zip(position, speed), reverse=True)

        stack = []; stack.append((target- lst[0][0]) / lst[0][1])

        for i in range (1, n):
            t = (target - lst[i][0]) / lst[i][1]
            if stack[-1] < t:
                stack.append(t)

        return len(stack)

# position을 기준으로 내림차순 정렬
# t 계산
# stack에 t를 하나씩 넣음
#   지금 들어온 t가 stack의 top보다 작다면
#       앞 차에 흡수, pop()
# len(stack) = fleet 개수

# 앞에 있는 차를 먼저 고려하려면, 앞에 있는 차를 먼저 계산하기
# 뒷 차가 더 빠르다면, 뒷 차가 걸리는 시간은 앞 차에게 종속된다.

# Time Complexiy: O(n log n)
# Space Complexity: O(n)