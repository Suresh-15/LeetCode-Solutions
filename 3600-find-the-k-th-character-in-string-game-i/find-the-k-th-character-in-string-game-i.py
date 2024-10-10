class Solution:
    def kthCharacter(self, k: int) -> str:
        nextChar = {
            'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 
            'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 
            'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 
            's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y',
            'y':'z', 'z':'a'
        }

        string = 'ab'
        appendString = 'b'
        while len(string) < k:
            for i in range(len(appendString)):
                appendString += nextChar[appendString[i]]
            string += appendString
    
        return string[k - 1]