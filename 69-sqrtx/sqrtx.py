import math

class Solution:
    def mySqrt(self, x: int) -> int:
        # return math.floor(math.sqrt(x))

        if x == 0 or x == 1:
            return x
        
        left, right = 0, x // 2 + 1
        for _ in range(x):
            root = (left + right) // 2
            if root*root <= x and (root + 1)*(root + 1) > x:
                break
            elif root*root > x:
                right = root
            else:
                left = root + 1
        return root