class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings, check if the strings have the same characters
        (can be different order)
        
        Algo 1 O(n log n):
        Sort both strings and compare

        Algo 2 O(n) - Dict:
        Put each char and its occurrence into a maps
        Compare both maps
        """
        return sorted(s) == sorted(t)
        # char_map_s = {}
        # char_map_t = {}
        
        # for char in s:
        #     if char in char_map_s:
        #         char_map_s[char] += 1
        #     else:
        #         char_map_s[char] = 1
        
        # for char in t:
        #     if char in char_map_t:
        #         char_map_t[char] += 1
        #     else:
        #         char_map_t[char] = 1

        # return char_map_s == char_map_t