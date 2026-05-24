class MinStack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][-1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        if len(self.stack) == 0: return None
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0: return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0: return None
        return self.stack[-1][-1]
        
        
# stack에 저장할 때, (val, current_min)을 함께 저장한다.

# Time Complexity: O(1)
# Space Compleixty: O(n)