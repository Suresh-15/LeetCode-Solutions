class Solution:
    def minimumSteps(self, s: str) -> int:
        white = 0
        total_swaps = 0

        for position, char in enumerate(s):
            if char == "0":
                total_swaps += position - white
                white += 1

        return total_swaps