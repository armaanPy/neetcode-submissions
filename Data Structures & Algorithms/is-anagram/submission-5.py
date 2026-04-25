class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort strings and compare
        return True if sorted(s) == sorted(t) else False