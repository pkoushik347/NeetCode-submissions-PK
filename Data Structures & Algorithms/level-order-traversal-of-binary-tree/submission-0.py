# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = [root]
        while q:
            sz = len(q)
            l = []
            for i in range(sz):
                node = q[0]
                q = q[1:]
                if (node.left):
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
                l.append(node.val)
            ans.append(l)
        return ans

