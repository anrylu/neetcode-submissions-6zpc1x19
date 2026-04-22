# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count total len
        total_len = 0
        node = head
        while node:
            total_len += 1
            node = node.next
        
        # check which node to remove
        if n > total_len: return head
        ret = ListNode()
        ret.next = head
        index_to_del = total_len - n
        node = ret.next
        prev_node = ret
        for _ in range(index_to_del):
            prev_node = node
            node = node.next
        prev_node.next = node.next

        return ret.next
