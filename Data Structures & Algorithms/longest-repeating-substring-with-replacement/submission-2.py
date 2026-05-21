class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0; left = right = 0; n = len(s)
        counter = defaultdict(int)

        while right < n:
            counter[s[right]] += 1
            if (right - left + 1) - max(counter.values()) > k:
                ans = max(right - left, ans)
                while (right - left + 1) - max(counter.values()) > k:
                    print(left, right, counter)
                    counter[s[left]] -= 1
                    left += 1

            right += 1
                
        return max(ans, right - left)
        
        
# 통일시켜야 하는 알파벳은 현재 윈도우에서 가장 많이 쓰인 알파벳
#   max(counter.values())로 뽑아낼 수 있다.
# (전체 윈도우 길이 = right - left + 1) - max(counter.values()) <= k 라면 윈도우 성공
# (전체 윈도우 길이) - max(counter.values()) > k 라면,
#   counter[s[left]] -= 1, left += 1 하면서 윈도우의 크기를 줄인다.