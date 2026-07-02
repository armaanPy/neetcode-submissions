class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Init two pointers; l, r - either ends of the string
        Compare both converging pointers
        If pointers don't match, skip both l and r pointer
            Compare the output of the skipped pointers 
            with the reverse of the skipped pointers
        Increment pointers
        """
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l+1:r+1]
                skipR = s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1
        return True