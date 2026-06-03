# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # dummy를 넣어 Empty input 방지
        dummy = ListNode(-1, head)
        slow = dummy; fast = dummy.next

        while fast:
            if slow == fast:
                return True

            slow = slow.next
            if fast.next == None:
                break
            fast = fast.next.next
            

        return False
        
# Cycle detection의 구현이네요

# 주소값을 set에 넣으면서 검사하다보면 금방 되긴 할 것 같은데

# Time Complexity: O(n)
# Space Complexity: O(1)