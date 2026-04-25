class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        [1, 2, 3, 3]
        [1, 2, 3]
        """
        return True if len(set(nums)) != len(nums) else False