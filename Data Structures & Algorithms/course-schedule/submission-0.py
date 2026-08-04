class Solution:
    d: dict

    def __init__(self):
        self.d = dict()

    def traverse(self, course: int) -> bool:
        queue = collections.deque(); queue.append(course)
        s = set()

        while queue:
            c = queue.popleft()
            if c not in self.d:
                return True

            s.add(c)
            
            for pre in self.d[c]:
                if pre in s:
                    return False

                queue.append(pre)



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        # 일단 초기세팅
        for c, pre in prerequisites:
            if c not in self.d:
                self.d[c] = []

            self.d[c].append(pre)
        
        result = []

        for i in range(len(prerequisites)):
            result.append(self.traverse(prerequisites[i][0]))

        return all(result)
        

# 선수과목에 대한 얘기구만
# 아, {선수과목 -> 과목} 으로 표현하면, 이건 방향이 있는 그래프로 해석할 수 있구나
# 그러면 되는 경우는 뭐고 안 되는 경우는 뭐지?
# 사이클이 생기면 안 된다? 그냥 그게 끝인가? 끝인가보다.
# 사이클을 탐지할 수 있는 알고리즘은.. 토끼와 거북이가 있긴 한데, 여기서는 여러 갈래로 갈 수 있으니까 못 쓴다.
# 딕셔너리로 그래프 만들고, 그걸 가지고 접근해야 할 것 같은데

# c1 = {c2, c3, c4}
# c2 = {c3, c4}
# c5 = {c2}
# c3 = {c7}
# c6 = {c1}

# 각 코스마다 한 바퀴씩 돌면서 사이클 생기면 False하는 방향으로 갈까