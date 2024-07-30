import math

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Brute Force Method
        ==================
        
        answers = list()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        a = list([nums[i], nums[j], nums[k]])
                        a.sort()
                        if a not in answers:
                            answers.append(a)
        return answers
        """

        nums.sort()
        answers = list()
        checked = math.inf
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1 
            if nums[i] == checked:
                continue
            if left > n - 2 or nums[i] > 0:
                break

            target = -1 * nums[i]
            seen = set()
            while left < right:
                if nums[left] in seen:
                    left += 1
                    continue
                if nums[right] in seen:
                    right -= 1
                    continue
                summation = nums[left] + nums[right]
                
                if summation == target:
                    answers.append([nums[i], nums[left], nums[right]])
                    seen.add(nums[left])
                    seen.add(nums[right])
                    left += 1
                elif summation > target:
                    right -= 1
                else:
                    left += 1
            checked = nums[i]
            
        return answers