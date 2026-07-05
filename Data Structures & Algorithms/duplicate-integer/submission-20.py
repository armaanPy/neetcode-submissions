class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array
        Return true if there are any duplicates, else false

        Compare the length of the array, with the length of a set array
        """
        return True if len(nums) > len(set(nums)) else False