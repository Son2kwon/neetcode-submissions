# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkBST(self, node: Optional[TreeNode], int_min: int, int_max: int) -> bool:
        if node == None:
            return True

        return node.val > int_min and node.val < int_max \
            and self.checkBST(node.left, int_min, node.val) \
            and self.checkBST(node.right, node.val, int_max)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, -1001, 1001)

# BST임을 확인하려면, 현재 노드와 비교해서 왼쪽은 전부 작고, 오른쪽은 전부 커야함
# 조상 노드들은 서브트리가 가질 수 있는 값들의 하한 / 상한을 정함

# Time Complexity: O(n)
# Space Complexity: O(n)