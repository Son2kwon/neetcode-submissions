class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M = len(nums1); N = len(nums2); 
        k = (M + N + 1) // 2; # 왼쪽에 들어갈 원소의 개수
        A: List[int]; B: List[int]

        # 얕은 복사로 O(1) 시간 만큼 걸림
        if M > N:
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2

        A = [float('-inf')] + A + [float('inf')]
        B = [float('-inf')] + B + [float('inf')]

        left = 0; right = len(A) - 1

        while left <= right:
            mid = left + (right - left) // 2
            j = k - mid # j는 B의 인덱스

            print("left: ", left, "right: ", right)
            
            # A의 Left_MAX > B의 Right_min 라면, right 움직임
            if A[mid] > B[j+1]:
                print(1)
                right = mid - 1
            # B의 Left_MAX > A의 Right_min 라면, left 움직임
            elif B[j] > A[mid + 1]:
                print("B[j]: ", B[j], "A[mid + 1]: ", A[mid + 1])
                left = mid + 1
            else:
                if (M+N) % 2 == 0:
                    return ((max(A[mid], B[j]) + min(A[mid + 1], B[j + 1])) / 2)
                else:
                    return float(max(A[mid], B[j]))

        
# 중앙값을 생각하지 말고, 양 배열에 들어가는 개수를 생각하자.
