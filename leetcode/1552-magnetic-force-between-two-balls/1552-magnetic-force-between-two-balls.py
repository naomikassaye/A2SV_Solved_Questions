class Solution:
 def maxDistance(self,position:List[int],m:int)->int:
  position.sort()
  l,r,ans=1,position[-1]-position[0],0
  def check(d):
   c,last=1,position[0]
   for i in range(1,len(position)):
    if position[i]-last>=d:
     c+=1
     last=position[i]
   return c>=m
  while l<=r:
   mid=(l+r)//2
   if check(mid):
    ans=mid
    l=mid+1
   else:
    r=mid-1
  return ans