class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inGoing = dict(); outGoing = dict()
        cost = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            inGoing[i] = []
            outGoing[i] = []

        for start, destination, fee in flights:
            outGoing[start].append(destination)
            inGoing[destination].append(start)
            cost[start][destination] = fee


        DP = [[float('inf') for _ in range(n)] for _ in range(k + 2)]

        DP[0][src] = 0

        for count in range(1, k + 2):
            for destination in range(n):
                start = inGoing[destination]
                for s in start:
                    DP[count][destination] = min(DP[count][destination], DP[count-1][s] + cost[s][destination])

        ans = float('inf')
        for i in range(k + 2):
            ans = min(ans, DP[i][dst])

        if ans == float('inf'): return -1
        else: return ans
            

        

# DP 접근
# DP[count][X]: X에 도착할 때까지 count를 사용해서 도착한 가장 작은 cost
# node는 n개, count는 k + 2개
# DP[count][X] = for src in nodes min(DP[count-1][src]) + cost
