# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        a: Optional[ListNode] = dummy
        b: Optional[ListNode] = dummy

        for i in range(0, n+1):
            a = a.next

        while a:
            a = a.next
            b = b.next

        b.next = b.next.next

        return dummy.next
        

# 하필 end에서부터 n번째 node를 삭제하라는...
# stack을 사용하면 space complexity O(n)으로 풀 수는 있겠다.
# 하지만 space complexity를 O(1)으로 풀려면...

# length - n = 지워야 할 index 번호 (0-indexed)
# O(m)으로 한 번 돌면서 length를 구한 후 (m: 데이터 개수)
# index를 구해서 지운다
# O(m)의 시간 복잡도, 2-way

# n 만큼 앞서서 출발하는 포인터 a와 head에서 출발하는 포인터 b
# a가 None이 될 때까지 옮기면 b는 딱 지우는 위치에서 멈춘다. -> dummy에서 출발하고 n+1로 계산하면 지우기 직전에 멈춘다.
# 결국 O(m)의 시간 복잡도, 2-way
# 이 방법이 더 섹시한 것 같으니까, 이 방법으로 풀어본다.

# Time Complexity: O(min(n, m-n)); m is the length of the list
# Space Complexity: O(1)