# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ret = ListNode()
        node1 = l1
        node2 = l2
        carry = 0
        while node1 or node2:
            val = carry
            if node1:
                val += node1.val
                node1 = node1.next
            if node2:
                val += node2.val
                node2 = node2.next
            node.next = ListNode(val%10)
            node = node.next
            carry = val//10
        if carry:
            node.next = ListNode(carry)

        return ret.next