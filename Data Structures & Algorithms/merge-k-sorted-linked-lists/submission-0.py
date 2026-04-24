# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]

        ret = ListNode()
        ret.next = lists[0]
        for i in range(1, k):
            prev_node = ret
            node1 = ret.next
            node2 = lists[i]
            while node1 and node2:
                if node1.val <= node2.val:
                    prev_node = node1
                    node1 = node1.next
                else:
                    tmp = node2.next
                    prev_node.next = node2
                    prev_node = node2
                    prev_node.next = node1
                    node2 = tmp
            while node2:
                prev_node.next  = node2
                prev_node = node2
                node2 = node2.next
        return ret.next
