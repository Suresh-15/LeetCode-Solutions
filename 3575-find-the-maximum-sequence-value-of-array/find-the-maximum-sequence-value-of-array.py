class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_num = max(nums)
        max_or_value = (1 << (max_num.bit_length())) - 1

        dp_forward = [{} for _ in range(n)]
        dp_backward = [{} for _ in range(n)]

        # Initialize dp_forward
        dp_forward[0][1] = {nums[0]}
        for l in range(2, k + 1):
            dp_forward[0][l] = set()
        for i in range(1, n):
            dp_forward[i][1] = dp_forward[i - 1][1] | {nums[i]}
            for l in range(2, k + 1):
                dp_forward[i][l] = dp_forward[i - 1][l] | {
                    or_val | nums[i] for or_val in dp_forward[i - 1][l - 1]
                }

        # Initialize dp_backward
        dp_backward[n - 1][1] = {nums[n - 1]}
        for l in range(2, k + 1):
            dp_backward[n - 1][l] = set()
        for i in range(n - 2, -1, -1):
            dp_backward[i][1] = dp_backward[i + 1][1] | {nums[i]}
            for l in range(2, k + 1):
                dp_backward[i][l] = dp_backward[i + 1][l] | {
                    or_val | nums[i] for or_val in dp_backward[i + 1][l - 1]
                }

        max_value = 0
        for i in range(k - 1, n - k):
            forward_ors = dp_forward[i][k] if k in dp_forward[i] else set()
            backward_ors = dp_backward[i + 1][k] if k in dp_backward[i + 1] else set()
            for or1 in forward_ors:
                for or2 in backward_ors:
                    max_value = max(max_value, or1 ^ or2)

        return max_value
