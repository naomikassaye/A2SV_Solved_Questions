class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans=0
        def traverse(node):
            nonlocal ans
            if not node:
                return True,0,float('inf'),float('-inf')
            
            l_bst,l_sum,l_min,l_max=traverse(node.left)
            r_bst,r_sum,r_min,r_max=traverse(node.right)
            
            if l_bst and r_bst and l_max<node.val<r_min:
                curr_sum=l_sum+r_sum+node.val
                ans=max(ans,curr_sum)
                return True,curr_sum,min(l_min,node.val),max(r_max,node.val)
            
            return False,0,0,0
            
        traverse(root)
        return ans