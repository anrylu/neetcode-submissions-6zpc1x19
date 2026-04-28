# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(node):
            if not node:
                return None
            max_v = max(p.val, q.val)
            min_v = min(p.val, q.val)
            if min_v<=node.val<=max_v:
                return node
            return traverse(node.left) or traverse(node.right)

        return traverse(root)