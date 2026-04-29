# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = -1
        def search(node):
            nonlocal ret, k
            if node.left:
                search(node.left)
            k -= 1
            if k == 0:
                ret = node.val
            if k > 0 and node.right:
                search(node.right)
        
        search(root)
        return ret
