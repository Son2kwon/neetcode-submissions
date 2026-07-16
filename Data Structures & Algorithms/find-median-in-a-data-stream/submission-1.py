class MedianFinder:
    nums: List[int]

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.nums, num)

    def findMedian(self) -> float:
        cur = []; n = len(self.nums)

        for i in range(0, n):
            cur.append(heapq.heappop(self.nums))
        
        median = 0.0; n = len(cur)

        if n % 2 == 0:
            median = (cur[n // 2 - 1] + cur [n // 2]) / 2
        else:
            median = cur[n // 2]

        for n in cur:
            heapq.heappush(self.nums, n)

        return float(median)
        
# 중앙값을 구하자
# 일단 들어오는 값들이 정렬되어 있어야 중앙값을 구함 -> heap
# addNum은 O(log n)으로 접근 가능
# findMedian은 O(n log n)으로 접근 가능 -> 나쁘지 않은데..?