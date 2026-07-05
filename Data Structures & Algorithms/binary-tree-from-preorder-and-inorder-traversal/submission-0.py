# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findInOrder(self, preorder: List[int], inorder: List[int]):
        idx = 0; n = len(inorder)
        for idx in range(0, n):
            if preorder[0] == inorder[idx]:
                break

        return preorder[1 : idx + 1], preorder[idx + 1 : ], inorder[0 : idx], inorder[idx + 1 : ]

    def build(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        l_preorder, r_preorder, l_inorder, r_inorder = self.findInOrder(preorder, inorder)
        root.left = self.build(l_preorder, l_inorder)
        root.right = self.build(r_preorder, r_inorder)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = self.build(preorder, inorder)

        return root



        

# preorder랑 inorder를 보고 tree를 작성해라 이건가
# preorder는 자기자신 -> left -> right
# inorder는 left -> 자기자신 -> right
# 순서 하나만 가지고는 tree가 확정이 안 돼서 2개를 준거구나.

# preorder에서 root를 잡고, inorder에서 그 root와 같은 값을 찾는다.
# inorder의 root를 기준으로 left, right으로 나눈다.
# preorder도 마찬가지로, inorder의 left와 right의 크기를 가지고 나눈다.
# left는 left대로 재귀, right는 right 대로 재귀