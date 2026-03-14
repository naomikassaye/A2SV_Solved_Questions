class Solution:
    def frequencySort(self, s: str) -> str:
        counts={}
        for char in s:
            counts[char]=counts.get(char,0)+1
        unq=list(counts.keys())
        unq.sort(key=lambda char:counts[char], reverse=True)
        res=[]
        for char in unq:
            res.append(char*counts[char])
        return "".join(res)
        