class Solution:
    def canConstruct(self, ransom: str, magazine: str) -> bool:
        inv={}
        for char in magazine:
            inv[char]=inv.get(char, 0) + 1

        for char in ransom:
            if inv.get(char,0)<=0:
                return False
            inv[char]-=1
        
        return True
        