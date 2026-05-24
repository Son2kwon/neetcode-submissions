class MinStack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0: return None
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0: return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0: return None
        return min(self.stack)
        
        
# push, pop, top 은 O(1)에 되겠는데, getMin은 어떻게 O(1)으로 하지..? 별도의 변수를 지정하지 않는 이상 O(1)은 불가능할텐데...
# stack을 어짜피 list로 구현했으니까, index만 저장한다거나...
# stack 2개를 쓰면 O(n)으로 getMin 구현이 가능은 한데...
# 일단 min 내장 함수를 쓰면 뭐.. 해결은 가능한데...