class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [c.lower() for c in s if c.isalnum()]
        k = 0
        r = len(res) - 1
        while k < len(res):
            if res[k] != res[r]:
                return False
            k += 1
            r -= 1
        return True
