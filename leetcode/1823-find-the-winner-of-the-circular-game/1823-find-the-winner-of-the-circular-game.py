class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        r=0
        for i in range(1,n+1):
            r=(r+k)%i
        return r+1