# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1, None); cur = ans

        carry = 0

        while l1 or l2 or carry == 1:
            a: int; b: int;
            if l1 == None: a = 0
            else: a = l1.val

            if l2 == None: b = 0
            else: b = l2.val

            result = a + b + carry

            carry = result // 10
            result = result % 10

            cur.next = ListNode(result) 

            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return ans.next

# 그냥 덧셈하면 될 것 같은데?
# 자릿수가 같으면 이렇게 풀면 되는데, 자릿수가 다르다면...

# Time Complexity: O(n)
# Space Complexity: O(n)
