# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_node(self, start: Optional[ListNode], nxt: Optional[ListNode]):
        cur = start; prev = None

        while cur != nxt:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        start.next = nxt

        return prev

        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        cur = head;
        prev = dummy
        prev_list = dummy

        while cur:
            start = cur
            count = 0

            while cur and count < k:
                count += 1
                prev = cur
                cur = cur.next

            if count == k:
                prev_list.next = self.reverse_node(start, cur)
                prev = start
                prev_list = prev
                
        return dummy.next

# reverse 할 때는 dummy 이용해서 하는 무언가가 있었는데...
# 포인터 2개를 써서 뒤집을 시작점과 끝점을 찾는다.
#   시작점: start / 끝점: prev / 다음 순서: cur