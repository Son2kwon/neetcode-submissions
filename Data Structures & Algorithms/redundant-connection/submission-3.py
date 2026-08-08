class Solution:
    def find(self, parent: List[int], node: int):
        index = node

        while index != parent[index]:
            index = parent[index]

        return index

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = []

        for i in range(n + 1):
            parent.append(i)

        for n1, n2 in edges:
            r1, r2 = self.find(parent, n1), self.find(parent, n2)
            if r1 == r2:
                return [n1, n2]
            else:
                parent[r1] = r2
        
# 엣지를 연결하기 전에, 두 node의 parent가 같다면 그 edge를 반환
# parent는 항상 node 1을 가리키도록 하자.

# for n1, n2 in edges:
#   if find(parent, n1) == find(parent, n2):
#       return [n1, n2]
#   else:
#       parent 배열 업데이트
#           두 node 중에서 더 큰 값을 a라 할 때, parent[a] = parent[b]
#           타고타고 올라가면서 parent 업데이트