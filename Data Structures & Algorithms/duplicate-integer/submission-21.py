class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Return true if any value in a list appears more than once, otherwise false

        [1, 2, 3, 3] -> true
        ::
        len(list) = 4
        len(set(list)) = 3
        """
        return True if len(nums) > len(set(nums)) else False