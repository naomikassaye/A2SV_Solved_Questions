class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counts = {}

        for day in responses:
            unq= set(day)
            for word in unq:
                counts[word] = counts.get(word, 0) + 1
        
        wordd = ""
        freqq = 0
        
        for word, freq in counts.items():
            if freq > freqq:
                freqq = freq
                wordd = word
            elif freq == freqq:
                if wordd == "" or word < wordd:
                    wordd = word
                    
        return wordd