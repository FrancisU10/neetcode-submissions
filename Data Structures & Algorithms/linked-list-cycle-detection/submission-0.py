# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashMap = {}
        i = 0
        while head:
            if head.val in hashMap:
                return True
            hashMap[i] = head.val
            head = head.next
            i += 1
        return False