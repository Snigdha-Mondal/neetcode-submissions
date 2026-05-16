class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=''.join([i.lower() for i in s if i.isalnum()])
        return s1==s1[::-1]