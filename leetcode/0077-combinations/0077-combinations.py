class Solution:
 def combine(self,n,k):
  r=[]
  def b(s,p):
   if len(p)==k:
    r.append(p[:])
    return
   for i in range(s,n+1):
    p.append(i)
    b(i+1,p)
    p.pop()
  b(1,[])
  return r