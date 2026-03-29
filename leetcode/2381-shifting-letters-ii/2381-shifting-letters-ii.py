class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val
      
        res = list(s)
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            net_pos = (ord(res[i]) - ord('a') + current_shift) % 26
            res[i] = chr(net_pos + ord('a'))
            
        return "".join(res)