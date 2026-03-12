class Solution:
    def findValidPair(self, s: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        for i in range(len(s) - 1):
            first = s[i]
            second = s[i+1]
            
            if first != second:
                if counts[first] == int(first) and counts[second] == int(second):
                    return first + second
                    
        return ""