class MyCircularDeque:
    def __init__(self,k:int):
        self.q=[0]*k
        self.k=k
        self.s=0
        self.f=0
        self.r=0

    def insertFront(self,v:int)->bool:
        if self.isFull():return False
        self.f=(self.f-1)%self.k
        self.q[self.f]=v
        self.s+=1
        return True

    def insertLast(self,v:int)->bool:
        if self.isFull():return False
        self.q[self.r]=v
        self.r=(self.r+1)%self.k
        self.s+=1
        return True

    def deleteFront(self)->bool:
        if self.isEmpty():return False
        self.f=(self.f+1)%self.k
        self.s-=1
        return True

    def deleteLast(self)->bool:
        if self.isEmpty():return False
        self.r=(self.r-1)%self.k
        self.s-=1
        return True

    def getFront(self)->int:
        return -1 if self.isEmpty() else self.q[self.f]

    def getRear(self)->int:
        return -1 if self.isEmpty() else self.q[(self.r-1)%self.k]

    def isEmpty(self)->bool:
        return self.s==0

    def isFull(self)->bool:
        return self.s==self.k