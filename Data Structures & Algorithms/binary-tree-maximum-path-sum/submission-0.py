# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -1000

        def traverse(node):
            nonlocal max_path_sum
            if not node:
                return 0
            ret = node.val
            left = traverse(node.left)
            ret = max(ret, node.val+left)
            right = traverse(node.right)
            ret = max(ret, node.val+right)
            max_path_sum = max(max_path_sum, ret, node.val+left+right)
            return ret
        traverse(root)
        return max_path_sum
