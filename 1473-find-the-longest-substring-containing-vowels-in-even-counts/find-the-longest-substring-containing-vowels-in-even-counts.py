class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        num_bitmasks = 0b100000
        char_masks = [0] * (ord("z") + 1)
        for i, c in enumerate("aeiou"):
            char_masks[ord(c)] = 1 << i

        curr_prefix = 0
        first_index_of = [-1] * num_bitmasks
        last_index_of = [-1] * num_bitmasks
        for i, c in enumerate(s):
            curr_prefix ^= char_masks[ord(c)]
            if first_index_of[curr_prefix] == -1:
                first_index_of[curr_prefix] = i
            last_index_of[curr_prefix] = i
        first_index_of[0] = -1

        return max(b - a for a, b in zip(first_index_of, last_index_of))
