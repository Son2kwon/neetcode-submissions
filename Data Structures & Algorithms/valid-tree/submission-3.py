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
            
            self.visited.add(node)

            for n in self.d[node]:
                if n not in self.visited:
                    self.q.append(n)
        
        return count == nodes


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        for i in range(n):
            self.d[i] = []

        e = len(edges)
        for i in range(e):
            n1, n2 = edges[i]

            self.d[n1].append(n2)
            self.d[n2].append(n1)
        

        self.q.append(0)
        return self.traverse(0, n)