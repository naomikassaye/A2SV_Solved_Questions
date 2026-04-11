class Solution:
    def removeNodes(self,head:Optional[ListNode])->Optional[ListNode]:
        s,c=[],head
        while c:
            while s and s[-1].val<c.val:s.pop()
            s.append(c);c=c.next
        for i in range(len(s)-1):s[i].next=s[i+1]
        s[-1].next=None
        return s[0]