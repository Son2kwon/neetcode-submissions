# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        return prev
        
    
# Singly Linked List라 함부로 접근하기 어렵네... 이중 루프로 돌리면 편하긴 한데
# tmp에 현재 노드 저장하고 다음 걸로 넘어간다면...

# Time Complexity: O(n-2) = O(n)
# Space Complexity: O(1)