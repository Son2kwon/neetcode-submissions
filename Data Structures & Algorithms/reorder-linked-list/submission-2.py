# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 중간 지점 찾기, 사이클 필요 x
        slow = head; fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        
        # 뒤의 Linked List 뒤집기
        prev = None
        cur = second_half

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 두 배열 합치기
        first = head
        second = prev

        while second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2


        

    
# dq를 사용하지 않고 푸는 방법
#   토끼와 거북이 알고리즘으로 중간 찾기
#   중간을 기준으로 뒤 리스트 뒤집기 -> 뒤집으면서 last node의 순환 깨짐, 두 포인터는 연결될 필요 x
#   하나씩 연결하기

# Time Complexity: O(n)
# Space Complexity: O(1)
