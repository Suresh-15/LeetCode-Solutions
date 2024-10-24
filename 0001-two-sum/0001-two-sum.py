class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = defaultdict(lambda: None)

        for ind in range(len(nums)):
            key = target - nums[ind]
            if dictionary[key] is not None:
                return [dictionary[key], ind]
            else:
                dictionary[nums[ind]] = ind