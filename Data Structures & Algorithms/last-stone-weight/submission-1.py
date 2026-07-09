class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for w in stones:
            heap.append(-w)
            heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1

            if x > y:
                heapq.heappush(heap, y - x)
        
        if len(heap) == 0:
            heap.append(0)

        return heap[0] * -1

# heap에 1개가 남을 때까지 계속 하라는거네.

# max_heap을 만든다
# 2개를 pop -> 먼저 pop한 무게가 x, 나중에 pop한 무게가 y -> x >= y
# x-y == 0 이면 그냥 끝, x-y > 0 이면 x-y를 heap에 새로 넣기