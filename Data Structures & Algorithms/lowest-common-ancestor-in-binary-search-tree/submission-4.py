# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # while root:    
        #     if p.val < root.val and q.val < root.val:
        #         root = root.left
        #     elif p.val > root.val and q.val > root.val:
        #         root = root.right
        #     else:
        #         return root

        if ((not root) or (root.val == p.val) or (root.val == q.val)):
            return root
        
        lc = self.lowestCommonAncestor(root.left, p, q)
        rc = self.lowestCommonAncestor(root.right, p, q)

        if (lc == None):
            return rc
        elif rc == None:
            return lc
        else:
            return root