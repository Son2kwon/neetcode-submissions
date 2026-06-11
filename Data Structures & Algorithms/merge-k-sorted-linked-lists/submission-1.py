# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return None

        dummy = ListNode(-1001, None)
        n = len(lists)

        for i in range(0, n):
            prev = dummy
            cur = prev.next
            target = lists[i]
            
            # 초기 조건
            if cur == None:
                prev.next = target
                continue
            
            while cur and target:
                while cur and target and cur.val <= target.val:
                    prev = cur
                    cur = cur.next
                # cur == None 이라는 것은 prev.next에 그냥 붙여주면 된다는 뜻
                if cur == None:
                    prev.next = target
                    break
                # target == None 이라는 것은 끝까지 갔다는 의미
                if target == None:
                    break
                else:
                    tmp = target.next
                    prev.next = target
                    target.next = cur

                    prev = prev.next
                    target = tmp
                    
        return dummy.next

# 호시노 무서워... 으헤~ 하던 호시노가 보고싶어...

# 예외 처리
# lists == None일 경우

# cur과 target을 비교
# 