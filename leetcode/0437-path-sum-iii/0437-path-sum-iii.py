class Solution:
 def pathSum(self,root,targetSum):
  self.r=0
  m={0:1}
  def f(n,s):
   if not n:
    return
   s+=n.val
   self.r+=m.get(s-targetSum,0)
   m[s]=m.get(s,0)+1
   f(n.left,s)
   f(n.right,s)
   m[s]-=1
  f(root,0)
  return self.r