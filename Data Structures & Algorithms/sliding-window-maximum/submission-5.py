class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []; left = 0; right = k - 1; max_idx = 0; n = len(nums);
        dq = deque(); dq.append(0)

        for i in range(1, k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        while right < n:
            # print(left, right, dq)
            ans.append(nums[dq[0]])

            left += 1
            right += 1

            # dq[0]가 window를 벗어났다면 빼줌
            if dq[0] < left:
                dq.popleft()
            
            # 새로 들어온 값을 deque에 업데이트
            while right < n and dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)

        return ans
            


# deque를 사용해서 max_idx를 업데이트하는 방법
# 