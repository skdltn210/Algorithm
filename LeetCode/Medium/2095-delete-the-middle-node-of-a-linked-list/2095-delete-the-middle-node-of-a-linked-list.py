# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        n=0
        current=head
        while current:
            current=current.next
            n+=1
        i=0
        current=head
        for i in range(n//2-1):
            current=current.next
        current.next=current.next.next
        return head