# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:  # cur와 cur.next가 모두 존재할 때 반복
            npn = cur.next.next  # next pair's node 
            second = cur.next    # cur의 다음 노드

            prev.next = second   # 이전 노드가 second노드를 가리킴
            second.next = cur    # second노드와 현재 노드 뒤집기
            cur.next = npn       # 현재 노드가 다음 쌍의 노드를 가리킴 

            prev = cur           # prev를 현재 노드로 이동
            cur = npn            # cur을 다음 쌍의 노드로 이동 
        
        return dummy.next