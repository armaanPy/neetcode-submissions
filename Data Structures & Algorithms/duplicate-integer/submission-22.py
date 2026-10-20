class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        The below solution is acceptable, however, if the duplicate value is on indexes
        0 or 1, then we still run through the entire list. If there are a million values
        it will take very long.
        """
        # return len(nums) > len(set(nums))
        """
        Create a set called seen
        Iterate through the list, and append nums to the set
        if a num is already in seen, return True, otherwise false
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False