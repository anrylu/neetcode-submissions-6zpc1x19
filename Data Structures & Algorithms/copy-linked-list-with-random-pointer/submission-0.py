"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = {}
        old_node = head
        while old_node:
            new_node = Node(old_node.val)
            old2new[old_node] = new_node
            old_node = old_node.next

        old_node = head
        while old_node:
            new_node = old2new[old_node]
            new_node.next = old2new.get(old_node.next, None)
            new_node.random = old2new.get(old_node.random, None)
            old_node = old_node.next
        return old2new.get(head, None)