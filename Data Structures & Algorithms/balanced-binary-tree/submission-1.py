# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans: bool = True

    def height(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0

        l_height = self.height(node.left)
        r_height = self.height(node.right)

        if abs(l_height - r_height) > 1:
            self.ans = False

        return max(l_height, r_height) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)

        return self.ans
        
# DFS로 넘어가면서 각 노드마다 판단을 하면 뭐...

# Time Complexity: O(n)
# Space Complexity: O(log n)