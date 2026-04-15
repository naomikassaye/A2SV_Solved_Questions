class Solution:
 def buildTree(self,preorder:List[int],inorder:List[int])->Optional[TreeNode]:
  if not inorder:
    return None
  v=preorder.pop(0)
  r=TreeNode(v)
  i=inorder.index(v)
  r.left=self.buildTree(preorder,inorder[:i])
  r.right=self.buildTree(preorder,inorder[i+1:])
  return r