class Solution:
 def subarraysWithKDistinct(self,nums:List[int],k:int)->int:
  def f(x):
   l,res,c=0,0,{}
   for r in range(len(nums)):
    c[nums[r]]=c.get(nums[r],0)+1
    while len(c)>x:
     c[nums[l]]-=1
     if c[nums[l]]==0:del c[nums[l]]
     l+=1
    res+=r-l+1
   return res
  return f(k)-f(k-1)