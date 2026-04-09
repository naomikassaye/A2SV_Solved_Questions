class Solution:
    def decodeString(self, s: str) -> str:
        st,cur_s,cur_n=[],"",0
        for c in s:
            if c.isdigit():
                cur_n=cur_n*10+int(c)
            elif c=='[':
                st.append((cur_s,cur_n))
                cur_s,cur_n="",0
            elif c==']':
                prev_s,n=st.pop()
                cur_s=prev_s+n*cur_s
            else:
                cur_s+=c
        return cur_s