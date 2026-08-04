class Solution:
    in_degree: List[int]
    d: dict
    q: collections.deque

    def __init__(self):
        self.in_degree = []
        self.d = dict()
        self.q = collections.deque()

    def tsort(self, numCourses: int) -> bool:
        count = 0
        while self.q:
            count += 1
            c = self.q.popleft()

            if c in self.d:
                for p in self.d[c]:
                    self.in_degree[p] -= 1
                    if self.in_degree[p] == 0:
                        self.q.append(p)
                        

        return count == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        self.in_degree = [0 for _ in range(numCourses)]

        for c, p in prerequisites:
            if p not in self.d:
                self.d[p] = []

            self.d[p].append(c)
            self.in_degree[c] += 1

        for i in range(numCourses):
            if self.in_degree[i] == 0:
                self.q.append(i)

        return self.tsort(numCourses)
        
# Kahn's algorithm
# 위상 정렬을 위한 알고리즘
# incoming degree가 0인 노드들부터 queue에 넣는다.
# while queue:
#   c = queue.popleft()
#   c 제거
#   c에 이웃한 노드들의 incoming degree 감소
#   c에 이웃한 노드 중, incoming degree가 0이 된 노드를 queue에 넣음
# 아직 그래프에 노드가 남았다면 False
# 그래프가 비었다면 True