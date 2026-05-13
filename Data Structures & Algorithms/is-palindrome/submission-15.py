class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(formatted) - 1

        while left < right:
            if formatted[left] != formatted[right]:
                return False
            left += 1
            right -= 1
        return True
        