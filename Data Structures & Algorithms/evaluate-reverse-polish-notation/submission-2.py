class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set(['+', '-', '*', '/'])

        for c in tokens:
            if c in operator:
                a = int(stack.pop())
                b = int(stack.pop())

                if c == "+":
                    stack.append(a + b)
                elif c == '-':
                    stack.append(b - a)
                elif c == '*':
                    stack.append(a * b)
                elif c == '/':
                    stack.append(math.trunc(b/a))

            else:
                print(int(c))
                stack.append(int(c))

        return stack[-1]
                
        
# 학교 과제로 많이 풀었던 문제
# 숫자라면 stack에 저장
# 연산이라면 두 숫자 pop후 연산, 다시 스택에 push
# 마지막에 stack에서 pop

# Time Complexity: O(n)
# Space Complexity: O(n)