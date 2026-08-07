class Solution:
    d: dict
    visited: set

    def __init__(self):
        self.d = dict()
        self.visited = set()

    def traverse(self, node: int):
        self.visited.add(node)

        for neighbor in self.d[node]:
            if neighbor not in self.visited:
                self.traverse(neighbor)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        for i in range(n):
            self.d[i] = []
            
        for n1, n2 in edges:
            self.d[n1].append(n2)
            self.d[n2].append(n1)

        ans = 0
        for node in self.d:
            if node not in self.visited:
                ans += 1
                self.traverse(node)

        return ans

# 저번 문제에서 하나의 트리임을 알아봤으니, 이번엔 서로 다른 몇 개의 그래프가 있는지 세 보라는 건데..
# DFS로 돌아다니면서 visited에 있으면 금방 빠져 나오는게 그나마 생각나는 방안

# 이렇게 풀면 edge가 있는 노드들은 계산이 되는데, edge 없는 별개의 노드는 계산이 안된다.
# 그러면, edge가 없는 노드를 찾을 필요가 있는데... 