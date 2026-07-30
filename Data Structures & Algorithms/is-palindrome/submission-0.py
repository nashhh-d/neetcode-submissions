class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for ch in s.lower():
            if ch.isalnum():
                new += ch

        return new == new[::-1]