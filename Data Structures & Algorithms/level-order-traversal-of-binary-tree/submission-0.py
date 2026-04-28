# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        ret = [[root.val]]
        while q:
            count = len(q)
            vals = []
            for _ in range(count):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    vals.append(node.right.val)
            if vals: ret.append(vals)
        return ret
