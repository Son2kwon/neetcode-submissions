# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans: int
    l: list(int)

    def __init__(self):
        self.ans = 0
        self.l = list()

    def DFS(self, node: TreeNode):
        if node == None:
            return

        self.ans += 1 # ans를 미리 +1 한 다음에, 만약 list의 값보다 작다면 ans -= 1로 맞춰줌

        for n in self.l:
            if n > node.val:
                self.ans -= 1
                break

        self.l.append(node.val)

        self.DFS(node.left)
        self.DFS(node.right)

        self.l.pop()

    def goodNodes(self, root: TreeNode) -> int:
        self.DFS(root)

        return self.ans


# DFS로 접근하는게 편해보이는 문제
#   한 단계씩 내려가면서 value들을 저장 -> 깊이가 깊어지면 체크하는데 오랜 시간이 걸리는데, 노드 수가 100개니까 할 만 할 지도..?

# 현재 node의 값이 list의 모든 값들보다 크다면 ans += 1
# list에 현재 node 값 저장
# left, right 호출
# 현재 node 값 삭제

# Time Complexity: O(n)
# Space Complexity: O(n)