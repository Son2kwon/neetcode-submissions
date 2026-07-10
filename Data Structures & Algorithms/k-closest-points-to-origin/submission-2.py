class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for l in points:
            x = l[0]; y = l[1];
            d = (x * x + y * y) * -1
            p = [d] + l

            if len(heap) < k:
                heapq.heappush(heap, p)
            elif heap[0][0] < d:
                heapq.heapreplace(heap, p)

        ans = []

        for p in heap:
            ans.append([p[1], p[2]])

        return ans

# 크기 k의 heap을 만들어서 반환하면 된다.
# 근데 heap의 비교를 어떻게 할 것인가?
#   공식문서를 보니까 힙에 튜플이 들어갈 수 있다는데...

# 애초에 최대힙으로 관리하면 되겠구나!

# heappush 할 때의 기준도 잡아줘야 할 것 같은데...
#   결국 __it__를 재정의해주라는... 문제는 point가 class가 아니라 그냥 리스트라는 점

# heap에 튜플이 들어갈 때, 첫번째 원소가 비교의 기준점이 된다는 것을 생각해보면
# heap에 넣을 때 첫번째 원소로 dis, 두번째 세번째 원소를 x, y로 두면 되긴 하겠다.

# 이렇게 하면 최대힙 못 쓰는데..

# 기본 heap은 최소힙 -> 최대힙을 사용해야 가장 먼 점을 빼고 할 수 있음.
#   distance 값을 음수로 두면 되잖아?

# Time Complexity: O(n log k)
# Space Complexity: O(k)