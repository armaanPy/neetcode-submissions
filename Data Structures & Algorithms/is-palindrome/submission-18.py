class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        format string -> lowercase, no spaces, alpha only
        init l, r pointers
        compare pointers and move them closer while l < r
        """
        fmt_s = [c.lower() for c in s if c.isalnum()]
        l = 0
        r = len(fmt_s) - 1

        while l < r:
            if fmt_s[l] != fmt_s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True