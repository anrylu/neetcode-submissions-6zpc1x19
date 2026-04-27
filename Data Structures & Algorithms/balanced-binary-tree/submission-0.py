# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node):
            if not node:
                return 0, True
            left, left_balanced = traverse(node.left)
            right, right_balanced = traverse(node.right)
            height = max(left, right) + 1
            balanced = left_balanced and right_balanced and abs(left-right)<=1
            return height, balanced
        _, balanced = traverse(root)
        return balanced
