class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        return str(int(num1) + int(num2))

        """
        result = ""
        l1, l2, carry = len(num1) - 1, len(num2) - 1, 0

        while l1 >= 0 or l2 >= 0 or carry > 0:
            n1 = int(num1[l1]) if l1 >= 0 else 0
            n2 = int(num2[l2]) if l2 >= 0 else 0
            add = n1 + n2 + carry
            carry = add // 10
            result = str(add % 10) + result
            l1 -= 1
            l2 -= 1

        return result
        """
