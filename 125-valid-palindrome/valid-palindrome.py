class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        return cleaned_s == cleaned_s[::-1]

        """
        l, s = list(s), ""
        for i in l:
            if i.isalnum():
                s += i
        s = s.lower()
        if s == s[::-1]:
            return True
        else:
            return False
        """