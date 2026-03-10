class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26
        
        for char in s:
            index = ord(char) - ord('a')
            count[index] += 1
            
        for char in t:
            index = ord(char) - ord('a')
            count[index] -= 1
            
        steps = 0
        for val in count:
            if val > 0:
                steps += val
                
        return steps