# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        Max = 0
        n = len(values)
        for i in range(n // 2):
            Max = max(Max, values[i] + values[n - 1 - i])
        
        return Max