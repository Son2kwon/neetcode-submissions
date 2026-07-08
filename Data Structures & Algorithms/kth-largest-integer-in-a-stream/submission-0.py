class KthLargest:
    heap: list
    k: int

    def __init__(self, k: int, nums: List[int]):
        self.heap = []

        for n in nums:
            heapq.heappush(self.heap, -n)

        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        print(self.heap)
        print(heapq.nsmallest(self.k, self.heap))
        return heapq.nsmallest(self.k, self.heap)[self.k - 1] * -1

# 힙을 써서 푼다면..

# 제일 처음 들어온 list를 힙으로 만들고
# 들어올 때마다 heapify 하면

# 파이썬은 최대힙을 따로 제공하지 않기 때문에, 모든 값들을 음수로 표현해서 저장한다.