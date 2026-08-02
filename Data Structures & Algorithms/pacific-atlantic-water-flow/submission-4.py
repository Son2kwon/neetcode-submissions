class Solution:
    pacific: List[List[bool]]
    atlantic: List[List[bool]]

    def __init__(self):
        self.pacific = []
        self.atlantic = []

    def findCandidates(self, row: int, col: int, row_max: int, col_max: int):
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        candidates = []

        for dr, dc in delta:
            nr = row + dr; nc = col + dc;
            if 0 <= nr < row_max and 0 <= nc < col_max:
                candidates.append([nr, nc])

        return candidates

    def pacificTraverse(self, heights: List[List[int]]):
        queue = collections.deque()
        row_max = len(heights); col_max = len(heights[0])

        for i in range(row_max):
            queue.append([i, 0])

        for i in range(col_max):
            queue.append([0, i])

        while queue:
            i, j = queue.popleft()

            candidates = self.findCandidates(i, j, row_max, col_max)

            for ni, nj in candidates:
                if heights[ni][nj] >= heights[i][j] and not self.pacific[ni][nj]:
                    self.pacific[ni][nj] = True
                    queue.append([ni, nj])

    def atlanticTraverse(self, heights: List[List[int]]):
        queue = collections.deque()
        row_max = len(heights); col_max = len(heights[0])

        for i in range(row_max):
            queue.append([i, col_max - 1])

        for i in range(col_max):
            queue.append([row_max - 1, i])

        while queue:
            i, j = queue.popleft()

            candidates = self.findCandidates(i, j, row_max, col_max)

            for ni, nj in candidates:
                if heights[ni][nj] >= heights[i][j] and not self.atlantic[ni][nj]:
                    self.atlantic[ni][nj] = True
                    queue.append([ni, nj])

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_max = len(heights); col_max = len(heights[0])
        self.pacific = [[False for _ in range(col_max)] for _ in range(row_max)]
        self.atlantic = [[False for _ in range(col_max)] for _ in range(row_max)]

        for i in range(row_max):
            self.pacific[i][0] = True
            self.atlantic[i][col_max - 1] = True

        for i in range(col_max):
            self.pacific[0][i] = True
            self.atlantic[row_max - 1][i] = True

        self.pacificTraverse(heights)
        self.atlanticTraverse(heights)
    
        ans = []

        for i in range(row_max):
            for j in range(col_max):
                if self.pacific[i][j] and self.atlantic[i][j]:
                    ans.append([i, j])

        return ans


        
# Pacific에 닿을 수 있는 칸들 set
# Atlantic에 닿을 수 있는 칸들 set
# 그 두 set의 교집합을 찾는다.

# Pacific을 O(V + E)로 한 번 돌면서 True로 변환
# Atlantic을 O(V + E)로 한 번 돌면서 True로 변환
# 2중 for 문 돌면서 둘 다 True면 self.ans에 append