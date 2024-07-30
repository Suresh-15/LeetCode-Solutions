class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = (left + (right - left) // 2)
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
        """

        if int(num**0.5) == num**0.5:
            return True
        else:
            return False
        
        