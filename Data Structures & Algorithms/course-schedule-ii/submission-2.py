class Solution:
    in_degree: List[int]
    d: dict
    q: collections.deque
    ans: List[int]

    def __init__(self):
        self.in_degree = []
        self.d = dict()
        self.q = collections.deque()
        self.ans = []

    def tsort(self, numCourses: int) -> bool:
        count = 0
        while self.q:
            count += 1
            c = self.q.popleft()
            self.ans.append(c)

            if c in self.d:
                for p in self.d[c]:
                    self.in_degree[p] -= 1
                    if self.in_degree[p] == 0:
                        self.q.append(p)
                        

        return count == numCourses

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.in_degree = [0 for _ in range(numCourses)]

        for c, p in prerequisites:
            if p not in self.d:
                self.d[p] = []

            self.d[p].append(c)
            self.in_degree[c] += 1

        for i in range(numCourses):
            if self.in_degree[i] == 0:
                self.q.append(i)
        if self.tsort(numCourses):
            return self.ans
        else:
            return []

# 일단 Kahn 알고리즘 사용해서 True/False + 위상 정렬 하라는 거네