class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                binary = list(str(bin(num))[2:])
                length = len(binary)
                if binary.count('1')  == length:
                    ans.append(num // 2)
                else:
                    for i in range(length):
                        if binary[length - i - 1] == '0':
                            binary[length - i] = '0'
                            break

                    binary = ''.join(binary)
                    ans.append(int(binary, 2)) 
            
        return ans

            