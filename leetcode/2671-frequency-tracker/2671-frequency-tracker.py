from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.cnt=defaultdict(int)
        self.fqs=defaultdict(int)

    def add(self,num:int)->None:
        old=self.cnt[num]
        if self.fqs[old]>0:self.fqs[old]-=1
        self.cnt[num]+=1
        self.fqs[self.cnt[num]]+=1

    def deleteOne(self,num:int)->None:
        if self.cnt[num]>0:
            old=self.cnt[num]
            self.fqs[old]-=1
            self.cnt[num]-=1
            self.fqs[self.cnt[num]]+=1

    def hasFrequency(self,fq:int)->bool:
        return self.fqs[fq]>0