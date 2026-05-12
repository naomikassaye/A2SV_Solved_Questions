from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt=Counter(words)
        h=[]
        for word,freq in cnt.items():
            heapq.heappush(h,WordFreq(freq,word))
            if len(h)>k:
                heapq.heappop(h)
        res=[]
        while h:
            res.append(heapq.heappop(h).word)
        return res[::-1]

class WordFreq:
    def __init__(self,freq,word):
        self.freq=freq
        self.word=word
    def __lt__(self,other):
        if self.freq==other.freq:
            return self.word>other.word
        return self.freq<other.freq