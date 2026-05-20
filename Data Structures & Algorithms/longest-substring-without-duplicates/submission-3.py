class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0; left = 0; right = 0;
        n = len(s); alpha = set()
            
        while right < n:
            if s[right] in alpha:
                ans = max(ans, len(alpha))
                while s[right] in alpha:
                    alpha.remove(s[left])
                    left += 1

            else:
                alpha.add(s[right])
                right += 1

        return max(ans, len(alpha))


# Sliding window는 내부 데이터를 재활용한다.
