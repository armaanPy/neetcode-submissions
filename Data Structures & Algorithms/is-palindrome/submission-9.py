class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "Was it a car or a cat I saw?"
        # "wasitacaroracatisaw"
        #  l                 r
        res = [c.lower() for c in s if c.isalnum()]
        l, r = 0, len(res) - 1

        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True