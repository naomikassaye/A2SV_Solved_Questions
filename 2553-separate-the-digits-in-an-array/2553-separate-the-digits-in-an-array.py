class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        
        for num in nums:
            divisor = 1
            while divisor <= num // 10:
                divisor *= 10
            
            while divisor > 0:
                digit = num // divisor   
                res.append(digit)

                num %= divisor          
                divisor //= 10                
        return res