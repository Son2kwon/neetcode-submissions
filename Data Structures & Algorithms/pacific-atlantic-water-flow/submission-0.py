class Solution:
    ans: List[List[int]]
    available: set

    def __init__(self):
        self.ans = []
        self.available = set()

    def findCandidates(self, row: int, col: int, row_max: int, col_max: int, visited: List[List[bool]], heights: List[List[int]]):
        
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        candidates = []
        for di, dj in delta:
            ni = row + di; nj = col + dj;
            if 0 <= ni < row_max and 0 <= nj < col_max and not visited[ni][nj] and heights[row][col] >= heights[ni][nj]:
                visited[ni][nj] = True
                candidates.append([ni, nj])

        return candidates

    # pacific에 닿을 수 있는 지 확인하는 함수
    def pacificTest(self, heights: List[List[int]], row: int, col: int, visited: List[List[bool]]) -> bool:
        if row == 0 or col == 0:
            return True

        visited[row][col] = True

        candidates = self.findCandidates(row, col, len(heights), len(heights[0]), visited, heights)

        results = [self.pacificTest(heights, i, j, visited) for i, j in candidates]

        if any(results):
            return True
        else:
            return False

    # Atlantic에 닿을 수 있는 지 확인하는 함수
    def atlanticTest(self, heights: List[List[int]], row: int, col: int, visited: List[List[bool]]) -> bool:
        if row == len(heights) - 1 or col == len(heights[0]) - 1:
            return True

        visited[row][col] = True

        candidates = self.findCandidates(row, col, len(heights), len(heights[0]), visited, heights)

        results = [self.atlanticTest(heights, i, j, visited) for i, j in candidates]

        if any(results):
            return True
        else:
            return False

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_max = len(heights); col_max = len(heights[0])
        for i in range(row_max):
            for j in range(col_max):
                pacificVisited = [[False for _ in range(0, col_max)]for _ in range(0, row_max)]
                atlanticVistied = [[False for _ in range(0, col_max)]for _ in range(0, row_max)]
                if self.pacificTest(heights, i, j, pacificVisited) and self.atlanticTest(heights, i, j, atlanticVistied):
                    self.ans.append([i, j])

        return self.ans

# 한 셀에서 출발해서, pacific 과 atlantic 둘 다 갈 수 있는가? 를 보는건데..

# 단순하게 생각한다면 각 칸에서 출발해서 도달할 수 있는 지를 보면 되는데, 좀 더 똑똑하게 풀 수 있을 것 같은데

# 어느 칸이 둘 다 도달 할 수 있다면 그 칸에 도달할 수 있는 칸도 둘 다 도달할 수 있다.
# right top 과 left bottom 은 둘 다 닿을 수 있다.
# 그렇다면? 그쪽에서 출발해서, 그 수보다 큰 애들만 계속 찾는다면?

# 일단 그렇게 찾고 난 후보 말고도 더 있다.

# O(V + E) 말고 백트래킹도 섞을 수 있지 않을까..?

# 각 칸마다 출발해보고, "둘 다 도달할 수 있는 칸 집합"에 속하는 칸에 도착하면 good, 아니라면 bad로 BFS를 한다면?
# 진짜 난 천재인가 싶다.

# 음.. BFS로 풀려니까 뭔가 "둘 다 닿는 것에 대해" 판단이 어렵다
# 이럴거면, DFS로 Pacific 한 번, DFS로 Atlantic 한 번 돌리는 게 더 나을 것 같은데?