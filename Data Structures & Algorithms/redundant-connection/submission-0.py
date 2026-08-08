class Solution:
    d: dict
    
    def __init__(self):
        self.d = dict()

    def checkCycle(self, n1: int) -> bool:
        visited = set()

        q = collections.deque()

        q.append(n1)

        while q:
            node = q.popleft()
            if node in visited:
                return True
            
            visited.add(node)

            for n in self.d[node]:
                if n not in visited:
                    q.append(n)

        return False


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        for i in range(n + 1):
            self.d[i] = []

        ans = []

        for n1, n2 in edges:
            self.d[n1].append(n2)
            self.d[n2].append(n1)
            
            if self.checkCycle(n1):
                ans = [n1, n2]
                break
        
        return ans


# 사이클에 포함된 애들 찾아서, 그 중 하나의 엣지를 삭제하라는 건데..
# 일단 edges를 기준으로 그래프 만들다가, 사이클 생기면 그 엣지를 빼고 만드는 식으로 가면..?
# 그러면 사이클을 어떻게 판단할까?
#   n1에서 출발해서 n1으로 다시 돌아오는 지 확인하기
#   