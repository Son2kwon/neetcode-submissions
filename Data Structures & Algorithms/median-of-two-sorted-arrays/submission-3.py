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

        left = 0; right = len(A)

        while left <= right:
            # mid와 j는 개수, 인덱스가 아님.
            mid = left + (right - left) // 2
            j = k - mid
            print("mid: ", mid)
            
            A_LEFT_MAX: int; A_right_min: int; B_LEFT_MAX: int; B_right_min: int;
            # A에서 왼쪽으로 하나도 안 가져온다면...
            if mid == 0:
                A_LEFT_MAX = float('-inf')
                if len(A) == 0: A_right_min = float('inf')
                else: A_right_min = A[mid]
            # A에서 왼쪽으로 전부 가져간다면...
            elif mid == len(A):
                A_LEFT_MAX = A[mid - 1]
                A_right_min = float('inf')
            else:
                A_LEFT_MAX = A[mid - 1]
                A_right_min = A[mid]

            if j == 0:
                B_LEFT_MAX = float('-inf')
                B_right_min = B[j]
            elif j == len(B):
                B_LEFT_MAX = B[j - 1]
                B_right_min = float('inf')
            else:
                B_LEFT_MAX = B[j - 1]
                B_right_min = B[j]

            if A_LEFT_MAX > B_right_min:
                right = mid - 1
            elif B_LEFT_MAX > A_right_min:
                left = mid + 1
            else:
                if (M + N) % 2 == 0:
                    return (max(A_LEFT_MAX, B_LEFT_MAX) + min(A_right_min, B_right_min)) / 2.0
                else:
                    return max(A_LEFT_MAX, B_LEFT_MAX)






        
# 중앙값을 생각하지 말고, 양 배열에 들어가는 개수를 생각하자.

# Time Complexity: O(log(m))
# Space Complexity: O(1)