class Solution:
    def sumEvenGrandparent(self,root:TreeNode)->int:
        s=0
        def d(n,p,g):
            nonlocal s
            if not n:
                return
            if g%2==0:
                s+=n.val
            d(n.left,n.val,p)
            d(n.right,n.val,p)
        d(root,1,1)
        return s