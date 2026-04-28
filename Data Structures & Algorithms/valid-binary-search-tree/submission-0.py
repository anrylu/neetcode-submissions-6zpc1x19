# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return True, None, None
            left_balanced, left_min, left_max = traverse(node.left)
            if not left_balanced:
                return False, None, None
            right_balanced, right_min, right_max = traverse(node.right)
            if not right_balanced:
                return False, None, None
            balanced = True
            if left_max is not None and node.val<=left_max:
                balanced = False
            if right_min is not None and node.val>=right_min:
                balanced = False
            min_v = node.val if left_min is None else left_min
            max_v = node.val if right_max is None else right_max
            return balanced, min_v, max_v
        is_valid, _, _ = traverse(root)
        return is_valid