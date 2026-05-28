class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0; right = len(nums) - 1; mid = 0;

        while left <= right:
            mid = left + (right - left) // 2

            # left mid right / x 인 경우 -> 한 번도 안 돌아감 -> mid = 0 반환
            if nums[left] < nums[mid] and nums[mid] < nums[right]:
                mid = 0
                break
            # left mid / right 인 경우 -> left 이동
            elif nums[left] < nums[mid] and nums[mid] > nums[right]:
                left = mid
            #left / mid right 인 경우 -> right 이동
            elif nums[left] > nums[mid] and nums[mid] < nums[right]:
                right = mid
            elif right - left == 1:
                if nums[left] > nums[right]:
                    mid = right
                else:
                    mid = left
                break
            # x / left mid right 인 경우 -> left 반환
            else:
                mid = left
                break

             

        
        return nums[mid]

        
        
# 이젠 하다하다 rotate를 시키네..
# rotate 한 것을 감안해서 계산을 한다면 그냥 풀 수 있을 것 같은데
#   i -> (i + 1) % n (3 -> (3 + 1) % 4 = 0)
#   k -> (k - 1) (0 -> (-1 + 4 * 1) = 3)
# 근데 python에서는 arr[-1] = arr[n - 1] 이니까 한 바퀴 안 쪽으로 돌 때는 상관 없다.
#   n 번 돌릴 때 len(arr) = k 라면, 실제로 도는 횟수는 n % k
#       n % k 의 결과는 0 ~ (n-1) 이니까 그냥 python 코드 그대로 써도 될 듯?
# 근데 시작이 1이나 0이 아니구나. 그러면 뭐, 위 방법은 못 쓰겠네. 몇 번 돌았는지 바로 알 수 있는 방법이 없으니.

# rotate를 하면 0 ~ k 까지 오름차순, k+1 ~ n-1 까지도 오름차순
# + (k+1 ~ n-1) < (0 ~ k)
#   min은 arr[k+1] -> 어디서 바뀌냐가 문제
#      이렇게 생각하면 Parameteric search에 가까운 것 같은데..?

# 위 내용들 중 중요한 것은
# (0~k), (k+1 ~ n-1) 로 구분할 수 있다는 점
# (0~k) > (k+1 ~ n-1) 라는 점
# ans = arr[k+1] 라는 점
# left mid / right => arr[left] < arr[mid] and arr[mid] > arr[right]: left = mid
# left / mid right => arr[left] > arr[mid] and arr[mid] < arr[right]: right = mid