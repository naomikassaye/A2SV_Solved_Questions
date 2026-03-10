class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n=num%3
        if n==0:
            x=num//3
            listt=[x-1, x, x+1]
            return listt
        else:
            listt=[]
            return listt

        