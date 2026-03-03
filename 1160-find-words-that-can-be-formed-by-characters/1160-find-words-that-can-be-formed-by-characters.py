from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charcount=Counter(chars)
        leng=0

        for word in words:
            wordcount=Counter(word)

            possible=True
            for letter in wordcount:
                if wordcount[letter]>charcount.get(letter,0):
                    possible=False
                    break
            if possible:
                leng+=len(word)
        return leng

        