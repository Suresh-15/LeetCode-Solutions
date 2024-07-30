class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        number = 0
        for i in digits:
            number = number * 10 + i
        number = number + 1
        string = str(number)
        digits = list([int(s) for s in string])
        return digits
        """

        carry = 0 
        for i in range(len(digits) - 1, -1, -1): 
            carry = 1 if digits[i] + 1 >= 10 else 0 
            digits[i] = (digits[i] + 1) % 10 
            if not carry: 
                break
        if carry: 
            digits.insert(0, 1)
        return digits