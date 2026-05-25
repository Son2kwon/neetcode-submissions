class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = []; n = len(position)
        for i in range(0, n):
            lst.append([position[i], speed[i]])

        lst.sort(key=lambda x : x[0], reverse=True)

        t = []

        for p, s in lst:
            time = (target - p) / s
            t.append(time)

        stack = []; stack.append(t[0])

        for i in range (1, n):
            if stack[-1] < t[i]:
                stack.append(t[i])

        return len(stack)

# position을 기준으로 내림차순 정렬
# t 계산
# stack에 t를 하나씩 넣음
#   지금 들어온 t가 stack의 top보다 작다면
#       앞 차에 흡수, pop()
# len(stack) = fleet 개수