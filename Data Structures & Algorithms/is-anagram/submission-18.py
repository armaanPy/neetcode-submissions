class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings, check if the strings have the same characters
        (can be different order)
        
        Algo 1 O(n log n):
        Sort both strings and compare

        Algo 2 O(n) - Two Pointer:
        ...
        """
        return sorted(s) == sorted(t)