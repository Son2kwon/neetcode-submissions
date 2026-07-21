class Solution:
    ans: List[str]

    def __init__(self):
        self.ans = []

    def backTrack(self, n: int, opened: int, closed: int, s: List[str]):
        if opened == n and closed == n:
            self.ans.append("".join(s))
            return

        if opened < n:
            s.append("(")
            self.backTrack(n, opened + 1, closed, s)
            s.pop()

        if opened > closed:
            s.append(")")
            self.backTrack(n, opened, closed + 1, s)
            s.pop()
        

    def generateParenthesis(self, n: int) -> List[str]:
        self.backTrack(n, 0, 0, [])

        return self.ans

# 지금까지 쓴 ( 의 개수 open
# 지금까지 쓴 ) 의 개수 close

# ( 를 하나 더 써도 되는 건: open < n 일때
# ) 를 하나 더 써도 되는 건: 안 닫힌 ( 가 있을 때, 즉 open > close 일 때
