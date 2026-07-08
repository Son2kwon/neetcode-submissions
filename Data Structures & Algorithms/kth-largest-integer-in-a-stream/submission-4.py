class KthLargest:
    heap: List[int]
    k: int

    def __init__(self, k: int, nums: List[int]):
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)
        print(self.heap)

        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        elif val >= self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]

# heap에는 k개의 원소만 담아둔다.