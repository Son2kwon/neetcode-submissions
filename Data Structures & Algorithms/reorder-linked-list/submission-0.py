# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dq = deque()
        cur = head

        while cur:
            dq.append(cur)
            cur = cur.next

        cur = ListNode(-1, head)

        while dq:
            n1: Optional[ListNode] = None; n2: Optional[ListNode] = None
            n1 = dq.popleft()
            if dq: n2 = dq.pop()

            cur.next = n1
            if n2: 
                n1.next = n2
                n2.next = None
            else:
                n1.next = None
            cur = n2

    
# 이것도 요리조리 next를 잘 기워넣으면 될 것 같은데
# Doubly Linked List 면 진짜 훨씬 쉬울텐데...
# Deque를 활용한다면 앞 뒤에서 한 번 씩 뽑으면 연결 될 것 같은데

# Time Limit이 걸리네. O(n)일텐데.
# 로직이 문제가 아니라, Output이 문제였구나
