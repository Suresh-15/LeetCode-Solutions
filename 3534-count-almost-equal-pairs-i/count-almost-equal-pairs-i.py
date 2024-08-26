class Solution:
    def check(self, num1, num2):
        first = str(num1)
        second = str(num2)

        while len(first) < len(second):
            first = "0" + first
        while len(second) < len(first):
            second = "0" + second

        diff_count = 0
        mismatch1 = -1
        mismatch2 = -1

        for i in range(len(first)):
            if first[i] != second[i]:
                diff_count += 1
                if diff_count == 1:
                    mismatch1 = i
                elif diff_count == 2:
                    mismatch2 = i
                else:
                    return False

        if diff_count == 2:
            first = list(first)
            first[mismatch1], first[mismatch2] = first[mismatch2], first[mismatch1]
            first = "".join(first)
        return first == second

    def countPairs(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] or self.check(nums[i], nums[j]):
                    count += 1
        return count
