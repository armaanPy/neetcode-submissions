class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a b c c b a
        # L         R
        res = [c.lower() for c in s if c.isalnum()]
        l = 0
        r = len(res) - 1

        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True