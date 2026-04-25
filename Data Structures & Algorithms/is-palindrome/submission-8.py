class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "Was it a car or a cat I saw?"
        # "wasitacaroracatIsaw"
        #  l                 r
        cleaned = [c.lower() for c in s if c.isalnum()]
        l, r = 0, len(cleaned) - 1

        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True