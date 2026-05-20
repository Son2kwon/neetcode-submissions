class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0; left = 0; right = 0; n = len(s); alpha = set();

        while right < n:
            if s[right] in alpha:
                ans = max(ans, len(alpha))
                left += 1
                right = left
                alpha = set()
            else:
                alpha.add(s[right])
                right += 1

        return max(ans, len(alpha))
            
        

# sliding window라고 해놓고 죄다 투 포인터 문제 밖에 없네...
# left, right 정해두고
# set에 지금까지 읽은 문자들을 넣어둠 (set은 찾는 게 O(1)이니까)
# set에 있다면 left = right으로 update

# 이렇게 풀다가 딱 걸렸네...
# left = right 이렇게 업데이트 하는게 아니라 left += 1 이렇게 업데이트를 한다면?
# 결국 O(n^2)으로 가겠네...
