class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 1: return True
        low, high = 0, n-1
        while low<high:
            while low<high and (not s[low].isalpha() and not s[low].isnumeric()):
                low += 1
            while low<high and (not s[high].isalpha() and not s[high].isnumeric()):
                high -= 1
            if s[low].lower() != s[high].lower(): return False
            low += 1
            high -= 1
        return True
