class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result=[]
        minsum=float('inf')
        for res1 in list1:
            for res2 in list2:
                if res1==res2:
                    i=list1.index(res1)
                    j=list2.index(res2)
                    idxsum=i+j

                    if idxsum<minsum:
                        minsum=idxsum
                        result=[res1]
                    elif idxsum==minsum:
                        result.append(res1)
        return result


        