# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    d: dict
    def __init__(self):
        self.d = {}

    def build(self, preorder: List[int], inorder: List[int], preorder_start: int, preorder_end: int, inorder_start: int, inorder_end: int) -> Optional[TreeNode]:
        if preorder_start > preorder_end or inorder_start > inorder_end:
            return None
            
        idx = self.d[preorder[preorder_start]]
        count = idx - inorder_start
        n = len(preorder)
        root = TreeNode(preorder[preorder_start])

        l_preorder_start = preorder_start + 1;  l_preorder_end = l_preorder_start + count - 1;
        l_inorder_start = inorder_start; l_inorder_end = idx - 1;

        r_preorder_start = l_preorder_end + 1; r_preorder_end = preorder_end;
        r_inorder_start = idx + 1; r_inorder_end = inorder_end;

        root.left = self.build(preorder, inorder, l_preorder_start, l_preorder_end, l_inorder_start, l_inorder_end)
        root.right = self.build(preorder, inorder, r_preorder_start, r_preorder_end, r_inorder_start, r_inorder_end)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        for i in range(0, n):
            self.d[inorder[i]] = i

        root = self.build(preorder, inorder, 0, n - 1, 0, n - 1)

        return root

# inorder에서 preorder의 현재 가장 첫번째 값의 idx를 찾는다 (root 찾기)
#   inorder의 왼쪽은 왼쪽 서브트리, 오른쪽은 오른쪽 서브트리
# preorder_start + 1 ~ inorder 왼쪽 서브트리의 개수 / 그 다음부터 끝까지 오른쪽 서브트리

# 현재 관심 있는 그 부분만 숫자로 표현하자면...
# inorder:  inorder_start ~ (idx - 1) / idx / idx + 1 ~ (n - 1)
# preorder: preorder_start / (preorder_start + 1) ~ (preorder_start + 1 + 개수 - 1) / (preorder_start + 1 + 개수) ~ (n - 1)
# (idx - 1 - inorder_start - 1) = 개수

# Time Complexity: O(n)
# Space Complexity: O(n)