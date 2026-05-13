class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Set converging pointers at both ends of the array
        Compare the squares of each pointer, append the bigger value to list
        If bigger value was right pointer, decrement
        If bigger value was left pointer, increment
        Continue
        Return reversed array (spliced for time complex)
        """
        left, right = 0, len(nums) - 1
        res = []

        while left <= right:
            if (nums[left] * nums[left]) > (nums[right] * nums[right]):
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1
        
        return res[::-1]

        # the first index is being skipped