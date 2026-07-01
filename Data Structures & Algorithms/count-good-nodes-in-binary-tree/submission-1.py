# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans: int

    def __init__(self):
        self.ans = 0

    def DFS(self, node: TreeNode, max_num: int):
        if node == None:
            return

        if node.val >= max_num:
            self.ans += 1
            max_num = node.val

        self.DFS(node.left, max_num)
        self.DFS(node.right, max_num)

    def goodNodes(self, root: TreeNode) -> int:
        max_num: int = -101
        self.DFS(root, max_num)

        return self.ans


# DFS로 접근하는게 편해보이는 문제
#   한 단계씩 내려가면서 value들을 저장 -> 깊이가 깊어지면 체크하는데 오랜 시간이 걸리는데, 노드 수가 100개니까 할 만 할 지도..?
# 현재 경로의 가장 큰 값만 저장한다면, 현재 node가 good인지 바로 체크 가능함.

# 

# Time Complexity: O(n)
# Space Complexity: O(n)