class MedianFinder:
    left_half: List[int]
    right_half: List[int]

    def __init__(self):
        self.left_half = []
        self.right_half = []

    def addNum(self, num: int) -> None:
        # 왼쪽에 없다면 그냥 바로 오른쪽에 넣는다. (첫 예외처리)
        if len(self.left_half) == 0:
            heapq.heappush(self.right_half, num)
        # 왼쪽이 존재하고, 큰 절반에 속한다면
        elif num >= self.right_half[0]:
            heapq.heappush(self.right_half, num)
        # 작은 절반에 속한다면
        else:
            heapq.heappush(self.left_half, -num)

        # 항상 1개 차이 나도록 관리를 하는데, right_half >= left_half 도록 관리
        # 그렇다면 저게 깨지는 경우는 2개
        # 1. right_half가 left_half보다 2개 많은 경우 -> right_half에서 left_half로 1개 옮김
        if len(self.right_half) - len(self.left_half) >= 2:
            t = heapq.heappop(self.right_half) * -1
            heapq.heappush(self.left_half, t)

        # 2. left_half가 right_half보다 1개 많은 경우 -> left_half에서 right_half로 1개 옮김
        elif len(self.left_half) > len(self.right_half):
            t = heapq.heappop(self.left_half) * -1
            heapq.heappush(self.right_half, t)


    def findMedian(self) -> float:
        n = len(self.left_half) + len(self.right_half)
        print(n)
        print(self.left_half)
        print(self.right_half)
        print()

        if n % 2 == 0:
            return ((self.left_half[0] * -1) + self.right_half[0]) / 2
        else:
            return float(self.right_half[0])
        
# 작은 절반은 max_heap, 큰 절반은 min_heap으로 관리한다면...

# addNum
#   들어오는 수가 어디에 들어가야 할 지 판단한 후에 넣음
#   항상 right_half가 더 많도록 관리 (right_half = left_half + 1)

# findMedian
#   n이 홀수라면 큰 절반에서 가져오고
#   n이 짝수라면 작은 절반 + 큰 절반