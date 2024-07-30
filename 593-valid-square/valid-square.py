import math


class Solution:
    def dist(self, p1: List[int], p2: List[int]) -> float:
        xpart = (p1[0] - p2[0]) ** 2
        ypart = (p1[1] - p2[1]) ** 2
        return math.sqrt(xpart + ypart)

    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        if p1==p2 or p1==p3 or p1==p4 or p2==p3 or p2==p4 or p3==p4:
            return False
        
        return len(set([self.dist(p1, p2), self.dist(p1, p3), self.dist(p1, p4), self.dist(p2, p3), self.dist(p2, p4), self.dist(p3, p4)])) == 2

        """

        p1_distances = sorted(list(set([self.dist(p1, p2), self.dist(p1, p3), self.dist(p1, p4)])))
        p2_distances = sorted(list(set([self.dist(p2, p1), self.dist(p2, p3), self.dist(p2, p4)])))
        p3_distances = sorted(list(set([self.dist(p3, p1), self.dist(p3, p2), self.dist(p3, p4)])))
        p4_distances = sorted(list(set([self.dist(p4, p1), self.dist(p4, p2), self.dist(p4, p3)])))

        if p1_distances != p2_distances or p2_distances != p3_distances or p3_distances != p4_distances:
            return False
        if len(p1_distances) != 2:
            return False
        if round(((math.sqrt(2)) * p1_distances[0]), 2) != round(p1_distances[1], 2):
            return False
        return True
 
        """