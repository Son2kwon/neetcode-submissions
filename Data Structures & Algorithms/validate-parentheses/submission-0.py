class Solution:
    def isValid(self, s: str) -> bool:
        stack = []; idx = 0; n = len(s)
        open_parantheses = set(['(', '{', '['])
        

        while idx < n:
            cur = s[idx]
            if cur in open_parantheses:
                stack.append(cur)
            else:
                if len(stack) == 0: return False

                top = stack.pop()
                if cur == ')' and top != '(': return False
                elif cur == '}' and top != '{': return False
                elif cur == ']' and top != '[': return False

            idx += 1

        return len(stack) == 0
        

# 학교 과제에서 너무 많이 한 거...
# 열린 괄호가 오면 stack에 push
# 닫힌 괄호가 오면 stack의 top 확인
#   stack이 비어있으면 false
#   stack의 top과 짝이 안 맞으면 false

# stack이 비어있으면 true, 아니라면 false