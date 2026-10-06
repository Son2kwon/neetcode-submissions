class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for src, dst in tickets:
            d[src].append(dst)

        for node in d:
            d[node].sort(reverse=True)

        stack = ["JFK"]; ans = []

        while stack:
            cur = stack[-1]

            if d[cur]:
                v = d[cur].pop()
                stack.append(v)
            else:
                ans.append(stack.pop())

        return ans[::-1]

        

        

# JKF부터 출발해, 모든 티켓을 사용해 모든 node를 들러라
# 한 노드에 여러 공항이 연결되어 있다면, lexical 상으로 작은 부분부터 돌아라

# 그냥 일방향으로 나가는 건 문제가 안 되는데, 다시 돌아오는 건 어떻게 처리할까?

# 힌트 1: 각 노드를 한 번씩 도는 그런 알고리즘을 사용해. smallest lexical order을 어떻게하면 보존할 수 있을까?
# 각 노드를 exaclty once visit 하는 알고리즘은 너무 많아. smallest lexical order는 각 node와 이어져 있는 min-heap을 사용하면 될 것 같은데..

# 현재 node append
# 다음 node = 현재 node의 이웃 중 lexcial minimum을 pop
# directed graph라 이건 쉽지 않다.

# 힌트 2: DFS를 사용하면서, neighbor 순서를 lexical 오름차순으로 먼저 정렬한다.
# 힌트 3: DFS는 naive solution. Perform DFS by removing the neighbor, traversing, reinserting
# 이게 대체 무슨 소리일까..

# 힌트 4: Hierholzer's Algorithm을 사용해보자.
# 한붓그리기라고 나오네..

# Hierholzer's algorithm
# 1. 시작점을 stack에 push
# 2. stack의 top에서 아직 안 쓴 edge가 있으면 그거 사용
# 3. 사용할 수 있는 edge가 없으면 정점에서 pop해서 경로에 추가
# 4. 모든 edge가 사용되면 역순으로 return