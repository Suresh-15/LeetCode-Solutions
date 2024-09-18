class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        zeros = False
        product = 1
        for i in nums:
            if i != 0:
                product *= i
            else:
                zeros = True
        
        result = []
        for i in nums:
            if i == 0:
                result.append(product)
            else:
                if zeros:
                    result.append(0)
                else:
                    result.append(product // i)

        return result