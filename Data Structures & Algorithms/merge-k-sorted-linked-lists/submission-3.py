# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0:
            return None

        k = len(lists); n = len(lists);
        i = 1

        while k > 1:
            for j in range(0, n, i*2):
                cur = lists[j]
                dummy = ListNode(-1001, cur)
                prev = dummy
                
                # Out of index인 경우 예외처리
                if (i + j) < n:
                    target = lists[j + i]
                else:
                    target = None

                # cur과 target 둘 중 하나라도 None 이라면 그냥 지나감
                if cur == None or target == None:
                    break
                while cur and target:
                    while cur and cur.val <= target.val:
                        prev = cur
                        cur = cur.next

                    # cur == None 이라면, prev에 target 연결하고 끝
                    if cur == None:
                        prev.next = target
                        break
                    
                    tmp = target.next
                    prev.next = target
                    target.next = cur

                    prev = prev.next
                    target = tmp

                lists[j] = dummy.next

            i *= 2
            k = (k+1)//2 # python 3의 round 함수는 round half to even -> 따라서 올림을 위해 다른 식으로 표현해야 함.
        
                    
        return lists[0]

# 역시 호시노는 무서울 때가 있어...

# Time Complexity: O(n log k)
# Space Complexity: O(1)