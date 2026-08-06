class Solution:
    in_degree: List[int]
    d: dict
    q: collections.deque
    visited: set

    def __init__(self):
        self.in_degree = []
        self.d = dict()
        self.q = collections.deque()
        self.visited = set()

    def traverse(self, root: int, nodes: int) -> bool:
        count = 0
        while self.q:
            count += 1
            node = self.q.popleft()
            
            if node in self.visited:
                return False
            
            self.visited.add(node)

            for n in self.d[node]:
                if n not in self.visited:
                    self.q.append(n)
        
        return count == nodes


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        for i in range(n):
            self.d[i] = []

        e = len(edges)
        for i in range(e):
            n1, n2 = edges[i]

            self.d[n1].append(n2)
            self.d[n2].append(n1)
        

        self.q.append(0)
        return self.traverse(0, n)

        

# 그래프가 트리처럼 쓰일라면, Cycle이 없어야 한다.
# 또 Cycle detection 문제야? 그러면 또 다시 Kahn 알고리즘을...
# 아 근데 Kahn 알고리즘은 DAG에서 쓰는 거구나... 그러면 여기서는 DFS + 백트래킹을 사용할까? 아니면 BFS?
# BFS로 접근하면서, 지금까지 체크한 애들을 set에 넣고, 검사를 하다가 set에 있는 원소를 본다면 False
# 그렇다면...

# 0인 node를 root로 잡고, queue에 넣는다.
# while queue:
#   node = queue.pop()
#   if node in set: return false
#   set.add(node)
#   for 이웃 in neighbors: if 이웃 not in set: queue.append(이웃)
# return True

# 아.. 모든 노드가 이어져있는 지도 봐야하지... 이건 뭐, root에서 출발해서 count를 세면 돼