class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=float('-inf')
        def f(n):
            nonlocal ans
            if not n:return 0
            l=max(0,f(n.left))
            r=max(0,f(n.right))
            ans=max(ans,n.val+l+r)
            return n.val+max(l,r)
        f(root)
        return ans