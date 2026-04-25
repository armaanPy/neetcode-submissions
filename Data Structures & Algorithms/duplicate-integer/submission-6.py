class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # len of nums vs len of set nums
        return True if len(nums) > len(set(nums)) else False