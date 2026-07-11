class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            elif heap[0] < n:
                heapq.heapreplace(heap, n)

        return heap[0]
        

# 같은 값도 다 포함하는 그런 최소을 만들라는 것 같은데

# k 크기의 최소힙을 만들어서 들어올 때마다 업데이트
# return heap[0]을 하면 k번째 큰 원소를 반환할 수 있겠다.