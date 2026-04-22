# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        node = head
        while node:
            tmp = node.next
            node.next = ret.next
            ret.next = node
            node = tmp
        return ret.next