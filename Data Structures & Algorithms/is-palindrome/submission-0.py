class Solution:
    def isPalindrome(self, s: str) -> bool:
        def clean(s):
            return "".join(i for i in s if i.isalnum())
        def rev(s):
            s = "".join(i for i in s if i.isalnum())
            return s[::-1]
        
        if clean(s).lower() == rev(s).lower():
            return True
        return False