class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows=1
        cend=points[0][1]

        for i in range(1, len(points)):
            if points[i][0]>cend:
                arrows+=1
                cend=points[i][1]
        return arrows

        