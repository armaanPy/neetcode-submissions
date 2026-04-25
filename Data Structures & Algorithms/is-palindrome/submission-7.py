class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a b c c b a
        # L         R
        res = [c.lower() for c in s if c.isalnum()]
        L, R = 0, len(res) -1
        while L < R:
            if res[L] != res[R]:
                return False
            L += 1
            R -= 1
        return True