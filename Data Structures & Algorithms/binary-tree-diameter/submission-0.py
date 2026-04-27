# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def traverse(node, links_to_root):
            nonlocal ret
            if not node:
                return 0
            left_len = traverse(node.left, links_to_root+1)
            right_len = traverse(node.right, links_to_root+1)
            ret = max(ret, links_to_root)
            ret = max(ret, left_len + right_len)
            return 1 + max(left_len, right_len)


        traverse(root, 0)
        return ret