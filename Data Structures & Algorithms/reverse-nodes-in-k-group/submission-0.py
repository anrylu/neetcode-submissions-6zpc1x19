# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check length
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        if n<k or k<=1:
            return head
        
        ret = ListNode()
        curr_head = ret
        curr_tail = ret
        node = head
        i = 0
        is_reverse = True
        while node:
            if i % k == 0:
                if (n-i) < k:
                    is_reverse = False
                else:
                    is_reverse = True
                curr_head = curr_tail
                curr_tail.next = node
                curr_tail = node
                node = node.next
                curr_tail.next = None
            else:
                if is_reverse:
                    tmp = node.next
                    node.next = curr_head.next
                    curr_head.next = node
                    node = tmp
                else:
                    curr_tail.next = node
                    curr_tail = node
                    node = node.next
            i += 1
        return ret.next