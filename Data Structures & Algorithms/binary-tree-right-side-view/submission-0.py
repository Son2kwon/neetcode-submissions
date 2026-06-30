# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        ans: List[int] = []
        q = collections.deque(); q.append(root)
        levels = 1 # 현재 level에 몇 개의 node가 있는지 저장하는 변수
        nxt_levels = 0 # 다음 level에 몇 개의 node가 있는지 저장하는 변수


        while len(q) > 0:
            ans.append(q[-1].val)
            for i in range(0, levels):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                    nxt_levels += 1
                if cur.right:
                    q.append(cur.right)
                    nxt_levels += 1

            levels = nxt_levels
            nxt_levels = 0

        return ans

        

# 대놓고 BFS를 노리는 문제가 나왔다...
# BFS는 queue + 반복문의 조합이라고 했으니까
# 각 level 별로 넣은 다음에, 그 level의 list[-1]을 가져오면 되는 문제

# Time Complexity: O(n)
# Space Complexity: O(2^h)