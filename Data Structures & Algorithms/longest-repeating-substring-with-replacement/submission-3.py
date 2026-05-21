class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0; left = right = 0; n = len(s)
        counter = defaultdict(int)
        max_freq = 0

        while right < n:
            counter[s[right]] += 1
            max_freq = max(max_freq, counter[s[right]])

            if (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1

            right += 1
            ans = max(ans, right - left)
                
        return ans
        
        
# 통일시켜야 하는 알파벳은 현재 윈도우에서 가장 많이 쓰인 알파벳
# max(counter.values())를 안 쓰고 max_freq라는 변수에 저장한다면?
#   max_freq 이상을 채우지 못하는 놈은 필요없다.

# Time Complexity: O(n)
# Space Complexity: O(k): k is the number of distinct alphabets