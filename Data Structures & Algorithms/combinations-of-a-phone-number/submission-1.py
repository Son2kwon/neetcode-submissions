class Solution:
    d: dict
    ans: List[str]

    def __init__(self):
        self.d = {
            2: ['a', 'b', 'c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
            }

        self.ans = []
    
    def backTrack(self, digits: str, depth: int, cur: List[str]):
        if depth == len(digits):
            self.ans.append("".join(cur))
            return

        n = len(self.d[int(digits[depth])])

        digit = int(digits[depth])
        for i in range(0, n):
            cur.append(self.d[digit][i])
            self.backTrack(digits, depth + 1, cur)
            cur.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        self.backTrack(digits, 0, [])
        return self.ans

# 각 숫자에 해당하는 알파벳으로 subset을 만든다고 해야하나?