class Solution:
    ans: List[List[str]]

    def __init__(self):
        self.ans = []

    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        l = start; r = end;

        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True

    def backTrack(self, s: str, start: int, cur: List[str]):
        n = len(s)
        if start == n:
            self.ans.append(cur.copy())

        for end in range(start + 1, n + 1):
            if self.isPalindrome(s, start, end - 1):
                cur.append(s[start: end])
                self.backTrack(s, end, cur)
                cur.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.backTrack(s, 0, [])
        return self.ans

# s[start: end]가 회문이라면 재귀
# 