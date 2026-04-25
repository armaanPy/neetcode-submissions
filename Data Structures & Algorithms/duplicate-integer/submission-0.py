class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # find len of original list
        # sort list and find len
        # if sorted list len < original list len return true
        x = len(nums)
        y = len(set(nums))
        if y < x:
            return True
        else:
            return False
