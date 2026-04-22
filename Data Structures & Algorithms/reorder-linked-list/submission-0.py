# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find length
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        if n <= 2: return

        # find the start of 2nd half part
        half = (n+1)//2
        i = 0
        prev_node = node = head
        while node and i<half:
            i += 1
            prev_node = node
            node = node.next
        prev_node.next = None
        
        # reverse this one
        second_half_root = ListNode()
        while node:
            tmp = node.next
            node.next = second_half_root.next
            second_half_root.next = node
            node = tmp
        
        # merge these two
        node1 = head
        node2 = second_half_root.next
        while node1 and node2:
            tmp1 = node1.next
            tmp2 = node2.next
            node1.next = node2
            node2.next = tmp1
            node1 = tmp1
            node2 = tmp2
        