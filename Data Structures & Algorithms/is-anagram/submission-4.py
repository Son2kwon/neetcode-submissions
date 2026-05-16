class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        arr = [0] * 26

        for c in s:
            arr[ord(c) - ord('a')] += 1
        
        for c in t:
            arr[ord(c) - ord('a')] -= 1

        for i in arr:
            if i != 0:
                return False

        return True

# Time Complexity: O(min(n, m)): n, m is a length of string
# Space Complexity: O(1)