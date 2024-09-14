class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers = set()
        temp = ''
        for i in word:
            if i.isnumeric():
                temp += i
            else:
                if temp != '':
                    numbers.add(int(temp))
                    temp = ''
        else:
            if temp != '':
                numbers.add(int(temp))

        return len(numbers)
