# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    global_max: int
    def __init__(self):
        self.global_max = float('-inf')

    def DFS(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0

        l = self.DFS(node.left)
        r = self.DFS(node.right)
        if l < 0:
            l = 0
        if r < 0:
            r = 0
            
        self.global_max = max(self.global_max, l + r + node.val)

        return max(l, r) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)

        return self.global_max

# (왼쪽에서 만드는 sum + 현재 값 + 오른쪽에서 만드는 sum) vs. global_max
# return 값은 둘 중에서 더 큰 값만 return