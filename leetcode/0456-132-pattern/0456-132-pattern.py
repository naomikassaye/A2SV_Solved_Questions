class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st,s3=[],float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<s3:
                return True
            while st and nums[i]>st[-1]:
                s3=st.pop()
            st.append(nums[i])
        return False