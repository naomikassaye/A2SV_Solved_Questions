class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()  
        n=len(skill)
        chemistry=0
        target=skill[0]+skill[-1]  

        left,right = 0,n - 1

        while left<right:
            if skill[left]+skill[right]!=target:
                return -1  
            chemistry+=skill[left]*skill[right]  
            left+=1
            right-=1

        return chemistry