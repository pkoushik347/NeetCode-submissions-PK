class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> float:
        def dfs(node, ans):
            if not node:
                return 0
            left = max(dfs(node.left, ans), 0)
            right = max(dfs(node.right, ans), 0)
            ans[0] = max(ans[0], node.val + left + right)
            return node.val + max(left, right)

        ans = [float('-inf')]
        dfs(root, ans)
        return ans[0]