from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        res=0
        for x,v in count.items():
            groups=(v+x)//(x+1)
            res+=groups*(x+1)
        return res