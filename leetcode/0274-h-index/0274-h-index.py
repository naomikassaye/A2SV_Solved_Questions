class Solution:
    def hIndex(self, cit: List[int]) -> int:
        cit.sort(reverse=True)
        h=0

        for i,c in enumerate(cit):
            rank=i+1
            if c>=rank:
                h=rank
            else:
                break
        return h
        