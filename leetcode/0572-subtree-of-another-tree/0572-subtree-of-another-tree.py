class Solution:
 def isSubtree(self,root,subRoot):
  def s(p,q):
   if not p and not q:
    return True
   if not p or not q or p.val!=q.val:
    return False
   return s(p.left,q.left) and s(p.right,q.right)
  if not root:
    return False
  if s(root,subRoot):
    return True
  return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)