class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        last = len(s)-1
        i = 0
        while i < last:
            if s[i] == s[last]:
                i+=1
                last-=1
            else:
                return False
        return True