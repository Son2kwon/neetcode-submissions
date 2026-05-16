class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t

# Time Complexity: O(n + m)
# Space Complexity: O(1)