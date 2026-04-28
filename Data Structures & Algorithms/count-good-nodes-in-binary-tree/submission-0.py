# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret = 0

        def traverse(node, max_v):
            nonlocal ret
            if not node:
                return
            if node.val >= max_v:
                ret += 1
            traverse(node.left, max(max_v, node.val))
            traverse(node.right, max(max_v, node.val))

        traverse(root, root.val)
        return ret