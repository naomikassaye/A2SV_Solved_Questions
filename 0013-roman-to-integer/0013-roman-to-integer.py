class Solution:
    def romanToInt(self, s: str) -> int:
        romanmap = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        total = 0
        n = len(s)

        for i in range(n):
            value = romanmap[s[i]]
           
            if i < n-1 and romanmap[s[i]] < romanmap[s[i+1]]:
                total -= value
            else:
                total += value

        return total