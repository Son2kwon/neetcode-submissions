# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    d: dict

    def __init__(self):
        self.d = defaultdict(list)

    def DFS(self, node: Optional[TreeNode], depth: int):
        if node == None:
            return

        self.d[depth].append(node.val)

        if node.left != None:
            self.DFS(node.left, depth + 1)
        if node.right != None:
            self.DFS(node.right, depth + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.DFS(root, 0)

        ans = list(list())

        for i in range (0, len(self.d)):
            ans.append(self.d[i])

        return ans
        

# BFS는 재귀를 쓰지 않는다. 재귀로 접근할거면 DFS를 쓰자. 그리고 난 재귀가 익숙하니까 DFS로 풀자.

# Time Complexity: O(n)
# Space Complexity: O(h)