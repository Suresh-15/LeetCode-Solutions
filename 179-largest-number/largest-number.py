from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_list = list(map(str, nums))

        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        str_list.sort(key=cmp_to_key(compare))
        largest_number = "".join(str_list)
        return largest_number if largest_number[0] != '0' else '0'
